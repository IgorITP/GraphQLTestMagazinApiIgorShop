from api.models import Users
from graphene_django.types import DjangoObjectType


class UserNode(DjangoObjectType):
    class Meta:
        model = Users
