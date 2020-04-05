import graphene
from django.contrib.auth import authenticate, login, logout

from main.schema.mutation import MainMutation
from ..models import User


class Registration(MainMutation):
    result = graphene.Boolean()

    class Input:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birth_date = graphene.String(required=True)
        sex = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate_and_get_payload(self, info, **kwargs):
        new_user = User.objects.create(
            first_name=kwargs['first_name'],
            last_name=kwargs['last_name'],
            birth_date=kwargs['birth_date'],
            sex=kwargs['sex'],
            email=kwargs['email']
        )

        password = kwargs.pop('password')
        new_user.set_password(password)
        new_user.save()
        return Registration(result=True)


class Login(graphene.Mutation):
    success = graphene.Boolean()

    class Meta:
        description = 'Вход пользователя в систему'

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        print(kwargs)
        user = authenticate(info.context, username=kwargs['email'], password=kwargs['password'])
        if user is not None:
            login(info.context, user)
        return Login(success=user is not None)


class Logout(graphene.Mutation):
    class Meta:
        description = 'Выход пользователя из системы'

    success = graphene.Boolean(required=True, description='Успех операции')

    @staticmethod
    def mutate(root, info):
        if info.context.user.is_authenticated:
            logout(info.context)
            return Logout(success=True)
        else:
            return Logout(success=False)


class EditUser(MainMutation):
    status = graphene.Boolean()

    class Input:
        user_id = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birth_date = graphene.String(required=True)
        sex = graphene.String(required=True)

    def mutate_and_get_payload(self, info, **kwargs):
        user = User.objects.get(id=kwargs['user_id'])

        user.first_name = kwargs['first_name']
        user.last_name = kwargs['last_name']
        user.birth_date = kwargs['birth_date']
        user.sex = kwargs['sex']
        user.save()

        return EditUser(status=True)


class Mutation(graphene.ObjectType):
    registration = Registration.Field()
    login = Login.Field()
    logout = Logout.Field()
    edit_user = EditUser.Field()
