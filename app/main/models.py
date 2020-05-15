import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class IngredientInfo(models.Model):
    WHERE = (
        ('F', 'Freezer'),
        ('R', 'Refrigerator'),
        ('T', 'Room Temperature')
    )

    name = models.CharField(max_length=50)
    keeping_days = models.PositiveIntegerField()
    kcalories = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/ingredients/')
    fridger = models.CharField(max_length=2, choices=WHERE)

    def __str__(self):
        return f'{self.name}'


class Ingredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.OneToOneField(IngredientInfo, on_delete=models.CASCADE)
    input_date = models.DateField()

    def __str__(self):
        return self.info.name

    def freshness(self):
        keeping_days = int(self.info.keeping_days)
        keeping_date = self.input_date + datetime.timedelta(days=keeping_days)
        left = keeping_date - datetime.datetime.today().date()
        left_days = left.days

        if keeping_days - left_days <= keeping_days * 0.3:
            return '신선도 높음'
        elif keeping_days - left_days <= keeping_days * 0.7:
            return '신선도 보통'
        elif keeping_days - left_days <= keeping_days:
            return '신선도 낮음'
        else:
            return '신선도 위험'

    def left_days(self):
        keeping_days = int(self.info.keeping_days)
        keeping_date = self.input_date + datetime.timedelta(days=keeping_days)
        left = keeping_date - datetime.datetime.today().date()
        left_days = left.days

        if keeping_days - left_days > keeping_days:
            return -left_days
        return left_days
