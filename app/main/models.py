import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    FRIDGER = (
        ('F', 'Freezer'),
        ('R', 'Refrigerator'),
        ('T', 'Room Temperature')
    )
    TYPE = (
        ('vegetables', '채소/과일'),
        ('meat', '육류'),
        ('marine', '수산물'),
        ('grain', '곡물/견과류'),
        ('sauce', '양념/소스'),
        ('milk', '가공/유제품'),
        ('others', '기타'),
    )

    name = models.CharField(max_length=50)
    keeping_days = models.PositiveIntegerField()
    kcalories = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/ingredients/')
    fridger = models.CharField(max_length=2, choices=FRIDGER)
    type = models.CharField(choices=TYPE, max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name


class MyStoredIngredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=True, null=True)
    input_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.ingredient.name

    def freshness(self):
        keeping_days = int(self.ingredient.keeping_days)
        keeping_date = self.input_date + datetime.timedelta(days=keeping_days)
        left = keeping_date - datetime.datetime.today().date()
        left_days = left.days

        if keeping_days - left_days <= keeping_days * 0.3:
            return '신선도 높음'
        elif keeping_days - left_days <= keeping_days * 0.7:
            return '신선도 보통'
        elif keeping_days - left_days <= keeping_days:
            return '신선도 낮음'
        return '신선도 위험'

    def left_days(self):
        keeping_days = int(self.ingredient.keeping_days)
        keeping_date = self.input_date + datetime.timedelta(days=keeping_days)
        left = keeping_date - datetime.datetime.today().date()
        left_days = left.days

        if keeping_days - left_days > keeping_days: return -left_days
        return left_days


class MyMemoIngredient(models.Model):
    STATUS = (
        ('checked', 'checked'),
        ('not_checked', 'not_checked'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=20, default='not_checked')


class RecommendedFood(models.Model):
    TYPE = (
        ('broth', '육수'),
        ('vegetables', '채소'),
        ('marine', '해산물'),
        ('meat', '고기/계란'),
        ('rice', '밥/쌀'),
        ('kimchi', '김치/발효'),
        ('dessert', '간식/디저트'),
    )

    user = models.ManyToManyField(User)
    name = models.CharField(max_length=30)
    ingredients_detail = models.CharField(max_length=200)
    ingredient = models.ManyToManyField(Ingredient, blank=True)
    recipe = models.TextField()
    type = models.CharField(choices=TYPE, max_length=30)

    def __str__(self):
        return self.name

    def user_count(self):
        return len(self.user.all())


class FoodComment(models.Model):
    food = models.ForeignKey(RecommendedFood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-pk',)

    def created_date(self):
        today = datetime.date.today()
        date = today - self.created_at
        return f'{date.days}일 전'
