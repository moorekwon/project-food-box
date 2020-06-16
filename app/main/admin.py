from django.contrib import admin

from main.models import Ingredient, MyStoredIngredient, MyMemoIngredient, RecommendedFood, FoodComment

admin.site.register(Ingredient)
admin.site.register(MyStoredIngredient)
admin.site.register(MyMemoIngredient)
admin.site.register(RecommendedFood)
admin.site.register(FoodComment)
