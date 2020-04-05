import graphene

from clients.models import Client
from clients.schema.types import ClientType
from main.decorators import check_auth


class Query(graphene.ObjectType):
    get_all_clients = graphene.List(ClientType)
    get_client = graphene.Field(ClientType, client_id=graphene.String(required=True))

    @check_auth
    def resolve_get_all_clients(self, info):
        return Client.objects.all()

    @check_auth
    def resolve_get_client(self, info, client_id):
        return Client.objects.get(id=client_id)

