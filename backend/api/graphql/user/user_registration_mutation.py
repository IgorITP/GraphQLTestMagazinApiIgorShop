import graphene
from api.models import Users


def is_have_email(email: str) -> bool:
    user = Users.objects.filter(email=email)
    if user:
        return True
    return False


def is_have_username(username: str) -> bool:
    user = Users.objects.filter(username=username)
    if user:
        return True
    return False


class UserRegistrationMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        first_name = graphene.String()

    registration = graphene.Boolean()
    error = graphene.String()

    @classmethod
    def mutate(cls, root, info, email, password, first_name, username):
        email = email.lower()
        try:
            error_msg = ""
            registration_status = False
            print('info', info)
            if is_have_email(email=email):
                error_msg = "Данный email уже зарегистрирован в системе"
            elif is_have_username(username=username):
                error_msg = "Данный username уже зарегистрирован в системе"
            else:
                Users.objects.create(
                    email=email,
                    password=password,
                    first_name=first_name,
                    username=username
                )
                registration_status = True
        except Exception as e:
            print(e)
            return None

        return UserRegistrationMutation(registration=registration_status, error=error_msg)
