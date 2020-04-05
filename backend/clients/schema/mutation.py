import graphene

from clients.models import Client
from main.schema.mutation import MainMutation


class CreateClient(graphene.Mutation):
    status = graphene.Boolean()

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birth_date = graphene.String(required=True)
        sex = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        Client.objects.create(
            first_name=kwargs['first_name'],
            last_name=kwargs['last_name'],
            birth_date=kwargs['birth_date'],
            sex=kwargs['sex'],
        )
        return CreateClient(status=True)


class EditClient(MainMutation):
    status = graphene.Boolean()

    class Input:
        id = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birth_date = graphene.String(required=True)
        sex = graphene.String(required=True)

    def mutate_and_get_payload(self, info, **kwargs):

        client = Client.objects.get(id=kwargs['id'])
        client.first_name = kwargs['first_name']
        client.last_name = kwargs['last_name']
        client.birth_date = kwargs['birth_date']
        client.sex = kwargs['sex']
        client.save()

        return EditClient(status=True)


class DeleteClient(MainMutation):
    status = graphene.Boolean()

    class Input:
        client_id = graphene.String(required=True)

    def mutate_and_get_payload(self, info, client_id):
        Client.objects.filter(id=client_id).delete()
        return DeleteClient(status=True)


class Mutation(graphene.ObjectType):
    create_client = CreateClient.Field()
    edit_client = EditClient.Field()
    delete_client = DeleteClient.Field()
