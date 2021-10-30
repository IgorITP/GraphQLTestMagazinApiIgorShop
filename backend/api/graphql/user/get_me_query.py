import graphene
from ..user import check_auth_token
from api.models import Users
from .user_node import UserNode
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
import jwt


class GetMeQuery(graphene.ObjectType):
    get_me = graphene.Field(UserNode)

    def resolve_get_me(self, info, **kwargs):
        info = check_auth_token(info=info)
        print('INFO: ', info)
        print('META FUNK', info.context.META)
        user = None
        username = info.context.META.get("username", None)
        if username is not None:
            print("KWARGS", kwargs)
            user = Users.objects.get(username=username)
        return user
