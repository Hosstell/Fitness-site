from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    email = models.CharField('Электронная почта', max_length=64, null=True, default=None, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, default=None)

