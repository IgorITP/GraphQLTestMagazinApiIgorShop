import graphene
from api.models import Users
from .user_node import UserNode


class GetMeQuery(graphene.ObjectType):
    get_me = graphene.Field(UserNode)

    def resolve_get_me(self, info, **kwargs):
        print('INFO: ', info)
        print('META FUNK', info.context.META)
        user = None
        email = info.context.META.get("email", None)
        if email is not None:
            print("KWARGS", kwargs)
            user = Users.objects.get(email=email)
        return user
