from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}: {self.full_price}'


class Plan(models.Model):
    PLANT_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )

    plan_type = models.CharField(choices=PLANT_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0,
                                                   validators=[
                                                       MaxValueValidator(100)
                                                   ])

    def __str__(self):
        return f'{self.plan_type}: {self.discount_percent}'


class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscription', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscription', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscription', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.client}, {self.service}, {self.plan},'
