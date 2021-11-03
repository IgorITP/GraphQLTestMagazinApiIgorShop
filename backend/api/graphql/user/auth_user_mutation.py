import graphene
from api.models import Users
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
import jwt
import time


def generate_jwt_token(user: Users):
    payload = {
        "email": user.email,
        "expired_at": time.time() + 900
    }
    jwt_token = jwt.encode(payload, settings.SECRET_KEY, 'HS256')

    return jwt_token


class AuthUserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    auth = graphene.Boolean()
    token = graphene.String()
    username = graphene.String()
    error = graphene.String()

    def mutate(self, info, email, password):
        print('info.', info.context.META)
        jwt_token = ""
        username = ""
        error = ""
        auth = False
        email = email.lower()
        user = Users.objects.filter(email=email)
        if user:
            user = user.first()
            if password == user.password:
                jwt_token = generate_jwt_token(user=user)
                auth = True
                username = user.username
            else:
                error = 'Неверный пароль'

        return AuthUserMutation(auth=auth, error=error, username=username, token=jwt_token)
