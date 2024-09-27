import graphene
from .category_node import CategoryNode
from api.models import Category


class GetCategoryQuery(graphene.ObjectType):
    get_category = graphene.Field(lambda: graphene.List(CategoryNode))

    def resolve_get_category(self, info):  #для нашего graphql запросов мы показываем какую информацию будет показывать при запросе
        print('info:', info)
        return Category.objects.all()
