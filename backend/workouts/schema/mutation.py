import graphene

from clients.models import Client
from main.schema.mutation import MainMutation
from workouts.models import Workout, WorkoutTime, SeasonTicket, WorkoutEvent
from workouts.schema.types import WorkoutTimeInputType


class CreateWorkout(MainMutation):
    status = graphene.Boolean()

    class Input:
        name = graphene.String(required=True)
        trainers = graphene.List(graphene.String, required=True)
        times = graphene.List(WorkoutTimeInputType, requied=True)

    def mutate_and_get_payload(self, info, **kwargs):

        new_workout = Workout.objects.create(name=kwargs['name'])
        new_workout.trainers.add(*kwargs['trainers'])

        for time in kwargs['times']:
            WorkoutTime.objects.create(
                weekday=WorkoutTime.get_eng_weekday_name(time['weekday']),
                time=time['time'],
                workout_id=new_workout.id
            )

        return CreateWorkout(status=True)


class EditWorkout(MainMutation):
    status = graphene.Boolean()

    class Input:
        id = graphene.String(required=True)
        name = graphene.String(required=True)
        trainers = graphene.List(graphene.String, required=True)
        times = graphene.List(WorkoutTimeInputType, requied=True)

    def mutate_and_get_payload(self, info, **kwargs):

        workout = Workout.objects.get(id=kwargs['id'])
        workout.trainers.clear()
        WorkoutTime.objects.filter(workout_id=workout.id).delete()

        workout.trainers.add(*kwargs['trainers'])
        for time in kwargs['times']:
            WorkoutTime.objects.create(
                weekday=WorkoutTime.get_eng_weekday_name(time['weekday']),
                time=time['time'],
                workout_id=workout.id
            )

        return EditWorkout(status=True)


class DeleteWorkout(MainMutation):
    status = graphene.Boolean()

    class Input:
        id = graphene.String(required=True)

    def mutate_and_get_payload(self, info, id):

        workout = Workout.objects.get(id=id)
        workout.trainers.clear()
        WorkoutTime.objects.filter(workout_id=workout.id).delete()
        workout.delete()

        return DeleteWorkout(status=True)


class CreateSeasonTicket(MainMutation):
    status = graphene.Boolean()

    class Input:
        client_id = graphene.String(required=True)
        workout_id = graphene.String(required=True)
        start_date = graphene.String(required=True)
        end_date = graphene.String(required=True)


    def mutate_and_get_payload(self, info, **kwargs):
        print(kwargs)

        SeasonTicket.objects.create(
            client_id=kwargs['client_id'],
            workout_id=kwargs['workout_id'],
            start_date=kwargs['start_date'],
            end_date=kwargs['end_date']
        )

        return CreateSeasonTicket(status=True)


class SaveSeasonTicket(MainMutation):
    status = graphene.Boolean()

    class Input:
        season_ticket_id = graphene.String(required=True)
        client_id = graphene.String(required=True)
        workout_id = graphene.String(required=True)
        start_date = graphene.String(required=True)
        end_date = graphene.String(required=True)

    def mutate_and_get_payload(self, info, **kwargs):
        print(kwargs)

        season_ticket = SeasonTicket.objects.get(id=kwargs['season_ticket_id'])

        season_ticket.client_id = kwargs['client_id']
        season_ticket.workout_id = kwargs['workout_id']
        season_ticket.start_date = kwargs['start_date']
        season_ticket.end_date = kwargs['end_date']
        season_ticket.save()

        return SaveSeasonTicket(status=True)


class DeleteSeasonTicket(MainMutation):
    status = graphene.Boolean()

    class Input:
        id = graphene.String(required=True)

    def mutate_and_get_payload(self, info, id):
        SeasonTicket.objects.filter(id=id).delete()
        return DeleteSeasonTicket(status=True)


class CreateEvent(MainMutation):
    status = graphene.Boolean()

    class Input:
        workout_id = graphene.String(required=True)
        date = graphene.String(required=True)
        time = graphene.String(required=True)
        trainers = graphene.List(graphene.String, required=True)
        clients = graphene.List(graphene.String, required=True)

    def mutate_and_get_payload(self, info, **kwargs):

        new_workout_event = WorkoutEvent.objects.create(
            workout_id=kwargs['workout_id'],
            date=kwargs['date'],
            time=kwargs['time'],
            creator_id=info.context.user.id
        )
        new_workout_event.trainers.add(*kwargs['trainers'])
        new_workout_event.clients.add(*kwargs['clients'])

        return CreateEvent(status=True)


class Mutation(graphene.ObjectType):
    create_workout = CreateWorkout.Field()
    edit_workout = EditWorkout.Field()
    delete_workout = DeleteWorkout.Field()
    create_season_ticket = CreateSeasonTicket.Field()
    save_season_ticket = SaveSeasonTicket.Field()
    delete_season_ticket = DeleteSeasonTicket.Field()
    create_event = CreateEvent.Field()
