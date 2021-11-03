from graphene_django.views import GraphQLView
from django.conf import settings
from app.models import Users
from django.db.models import Q
import jwt

algorithm = "HS256"


class TokenAuthGraphQLView(GraphQLView):
    def get_context(self, request):
        print('request.META', request.META)
        token = request.META.get('HTTP_AUTHORIZATION')
        print('token:', token)
        if token is not None:
            token = token.split('JWT ')[1]
            decode_token = jwt.decode(token, settings.SECRET_KEY, algorithms=[algorithm])
            print('decode_token', decode_token)
            user = Users.objects.filter(email=decode_token['email'])
            if user:
                user = user.first()
                request.META['username'] = user.username
                print('auth:', request.META['username'])
                print('new REQUEST', request.META)
        return request
