import graphene

from main.decorators import check_auth
from .types import UserType
from ..models import User


class Query(graphene.ObjectType):
    get_current_user = graphene.Field(UserType)
    get_all_users = graphene.List(UserType)

    def resolve_get_current_user(self, info):
        return info.context.user

    @check_auth
    def resolve_get_all_users(self, info):
        print('client')
        return User.objects.all()