from .user_registration_mutation import UserRegistrationMutation
from .auth_user_mutation import AuthUserMutation
import graphene


class UserMutation(graphene.ObjectType):
    user_registration_mutation = UserRegistrationMutation.Field()
    auth_user_mutation = AuthUserMutation.Field()
