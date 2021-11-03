import graphene
from .category_node import CategoryNode
from api.models import Category


class GetCategoryQuery(graphene.ObjectType):
    get_category = graphene.Field(lambda: graphene.List(CategoryNode))

    def resolve_get_category(self, info):
        print('info:', info)
        return Category.objects.all()
