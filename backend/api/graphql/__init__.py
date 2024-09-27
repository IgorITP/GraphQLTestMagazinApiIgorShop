from .user.user_mutations import UserMutation
from .user.get_me_query import GetMeQuery

from .basket.get_basket_query import GetBasketQuery
from .product.query_get_list_product import GetProductQuery


class ApiQuery(
    GetBasketQuery,
    GetMeQuery
):
    pass


class ApiMutation(
    UserMutation
):
    pass
