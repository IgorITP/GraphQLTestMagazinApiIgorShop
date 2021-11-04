from graphene_django.views import GraphQLView
from django.conf import settings
from api.models import Users
import jwt

algorithm = "HS256"


# GraphQLView базовый класс graphene_django, в котором мы перезаписывваем получение контекста запроса
class TokenAuthGraphQLView(GraphQLView):
    def get_context(self, request):
        print('request.META', request.META)
        token = request.META.get('HTTP_AUTHORIZATION',
                                 None)  # берем указанный JWT в Authorization при помощи функции get()
        print('token:', token)
        if token is not None:
            token = token.split('JWT ')[1]
            decode_token = jwt.decode(token, settings.SECRET_KEY,
                                      algorithms=[algorithm])  # декодим JWT токен и смотри что внутри
            print('decode_token', decode_token)
            user = Users.objects.filter(email=decode_token['email'])  # проверяем узера в базе данные при помощи filter
            if user:
                user = user.first()
                request.META['username'] = user.username
                print('auth:', request.META['username'])  # кладем в контекст запроса username пользователя
                print('new REQUEST', request.META)
        return request
