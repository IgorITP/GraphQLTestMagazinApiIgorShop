from api.graphql import ApiQuery, ApiMutation
import graphene

print('GRAPHQL')


class Mutation(ApiMutation, graphene.ObjectType):
    alive = graphene.Boolean()

    def resolve_alive(self, info):
        print('info', info.field_name)
        print(type(ApiMutation.user_registration_mutation))
        return True


class Query(ApiQuery, graphene.ObjectType):
    alive = graphene.Boolean()

    def resolve_alive(self, info):
        return True


schema = graphene.Schema(query=Query, mutation=Mutation)

