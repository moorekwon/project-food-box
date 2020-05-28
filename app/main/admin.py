from django.contrib import admin

from main.models import Ingredient, MyStoredIngredient, MyMemoIngredient, RecommendedFood


@admin.register(MyStoredIngredient)
class MyStoredIngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(MyMemoIngredient)
class MyMemoIngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(RecommendedFood)
class RecommendedFoodAdmin(admin.ModelAdmin):
    pass
