from graphene_django import DjangoObjectType

from clients.models import Client


class ClientType(DjangoObjectType):
    class Meta:
        model = Client
