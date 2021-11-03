from api.models import Product
from graphene_django.types import DjangoObjectType


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
