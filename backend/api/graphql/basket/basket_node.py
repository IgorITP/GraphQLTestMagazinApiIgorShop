from api.models import Basket
from graphene_django.types import DjangoObjectType


class BasketNode(DjangoObjectType):
    class Meta:
        model = Basket
