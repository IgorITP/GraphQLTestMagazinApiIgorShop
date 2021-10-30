import graphene
from .basket_node import BasketNode
from api.models import Basket


class GetBasketQuery(graphene.ObjectType):
    get_basket = graphene.Field(lambda: graphene.List(BasketNode))

    def resolve_get_basket(self, info):
        print('info:', info)
        return Basket.objects.all()
