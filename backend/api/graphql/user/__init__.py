from django.contrib.auth.hashers import check_password
from api.models import Users
from django.conf import settings
import jwt

algorithm = "HS256"


def get_email_from_jwt_token(decode_token: dict) -> str:
    email = decode_token.get('email', "")
    return email


def get_password_from_jwt_token(decode_token: dict) -> str:
    password = decode_token.get('password', "")
    return password


def check_auth_token_decorate(function_to_decorate):
    def the_wrapper_around_the_original_function(*args, **kwargs):
        print('META', args[1].context.META)
        token = args[1].context.META.get('HTTP_AUTHORIZATION')
        if token is None or token == "" or ' ' not in token:
            raise Exception("Вы не авторизированы")
        else:
            token = token.split('JWT ')[1]
            decode_token = jwt.decode(token, settings.SECRET_KEY, algorithms=algorithm)
            email = get_email_from_jwt_token(decode_token=decode_token)
            password = get_password_from_jwt_token(decode_token=decode_token)
            user = Users.objects.filter(email=email)
            if user:
                user = user.first()
                if check_password(password=password, encoded=user.password):
                    args[1].context.META['username'] = user.username
                    function_to_decorate(*args, **kwargs)
                else:
                    raise Exception("Пароли или Email не верны")
            else:
                raise Exception("Данного пользователя нет в системе")

    return the_wrapper_around_the_original_function


def check_auth_token(info):
    token = info.context.META.get('HTTP_AUTHORIZATION')
    if token is None or token == "" or ' ' not in token:
        raise Exception("Вы не авторизированы")
    else:
        token = token.split('JWT ')[1]
        decode_token = jwt.decode(token, settings.SECRET_KEY, algorithms=algorithm)
        email = get_email_from_jwt_token(decode_token=decode_token)
        password = get_password_from_jwt_token(decode_token=decode_token)
        user = Users.objects.filter(email=email)
        if user:
            user = user.first()
            if check_password(password=password, encoded=user.password):
                info.context.META['username'] = user.username
                return info
            else:
                raise Exception("Пароли или Email не верны")
        else:
            raise Exception("Данного пользователя нет в системе")
