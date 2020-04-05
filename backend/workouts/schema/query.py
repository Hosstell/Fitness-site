import graphene

from main.decorators import check_auth
from .types import WorkoutType, SeasonTicketType, WorkoutEventType
from ..models import Workout, SeasonTicket, WorkoutEvent


class Query(graphene.ObjectType):
    get_current_workout = graphene.Field(WorkoutType, workout_id=graphene.String(required=True))
    get_all_workouts = graphene.List(WorkoutType)
    get_season_tickets = graphene.List(SeasonTicketType, workout_id=graphene.String(required=True))
    get_current_season_ticket = graphene.Field(SeasonTicketType, season_ticket_id=graphene.String(required=True))
    get_all_events = graphene.List(WorkoutEventType)
    get_all_workout_of_user = graphene.List(WorkoutType)
    get_all_workout_events_of_user = graphene.List(WorkoutEventType)

    @check_auth
    def resolve_get_current_workout(self, info, workout_id):
        return Workout.objects.get(id=workout_id)

    @check_auth
    def resolve_get_all_workouts(self, info):
        return Workout.objects.all()

    @check_auth
    def resolve_get_season_tickets(self, info, workout_id):
        return SeasonTicket.objects.filter(workout_id=workout_id)

    @check_auth
    def resolve_get_current_season_ticket(self, info, season_ticket_id):
        return SeasonTicket.objects.get(id=season_ticket_id)

    @check_auth
    def resolve_get_all_events(self, info):
        return WorkoutEvent.objects.all()

    @check_auth
    def resolve_get_all_workout_of_user(self, info):
        return Workout.objects.filter(trainers=info.context.user)

    @check_auth
    def resolve_get_all_workout_events_of_user(self, info):
        return WorkoutEvent.objects.filter(trainers=info.context.user).order_by('-date')
