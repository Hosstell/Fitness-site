from django.db import models

from clients.models import Client
from users.models import User


class Workout(models.Model):
    name = models.CharField(max_length=50)
    trainers = models.ManyToManyField(User)


class WorkoutTime(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)

    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'
    WEEKDAYS = (
        (MONDAY, 'Понедельник'),
        (TUESDAY, 'Вторник'),
        (WEDNESDAY, 'Среда'),
        (THURSDAY, 'Четверг'),
        (FRIDAY, 'Пятница'),
        (SATURDAY, 'Суббота'),
        (SUNDAY, 'Воскресенье'),
    )
    weekday = models.CharField(max_length=15, choices=WEEKDAYS)
    time = models.TimeField()

    def get_rus_weekday_name(self):
        weekday = list(filter(lambda x: x[0] == self.weekday, self.WEEKDAYS))
        if weekday:
            return weekday[0][1]

    @classmethod
    def get_eng_weekday_name(cls, rus_weekday_name):
        weekday = list(filter(lambda x: x[1] == rus_weekday_name, cls.WEEKDAYS))
        if weekday:
            return weekday[0][0]


class WorkoutEvent(models.Model):
    date = models.DateField()
    time = models.TimeField()
    clients = models.ManyToManyField(Client)
    trainers = models.ManyToManyField(User)
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')
    create_date = models.DateTimeField(auto_now_add=True)


class SeasonTicket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
