import graphene
from graphene_django import DjangoObjectType

from workouts.models import Workout, WorkoutTime, SeasonTicket, WorkoutEvent


class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout


class SeasonTicketType(DjangoObjectType):
    class Meta:
        model = SeasonTicket


class WorkoutEventType(DjangoObjectType):
    class Meta:
        model = WorkoutEvent


class WorkoutTimeType(DjangoObjectType):
    class Meta:
        model = WorkoutTime

    rus_weekday = graphene.String()

    def resolve_rus_weekday(self, info):
        return self.get_rus_weekday_name()


class WorkoutTimeInputType(graphene.InputObjectType):
    weekday = graphene.String(required=True)
    time = graphene.String(required=True)

