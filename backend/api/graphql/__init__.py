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


def check_auth_token(function_to_decorate):
    def the_wrapper_around_the_original_function(*args, **kwargs):
        print('args', args)
        print('kwargs', kwargs)
        function_to_decorate(*args, **kwargs)
        print('DONE')

    return the_wrapper_around_the_original_function
