import graphene
from .product_node import ProductNode
from api.models import Product


class GetProductQuery(graphene.ObjectType):
    get_products = graphene.Field(lambda: graphene.List(ProductNode))

    def resolve_get_product(self, info):
        print('info:', info)
        return Product.objects.all()
