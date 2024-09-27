from api.models import Category
from graphene_django.types import DjangoObjectType


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
