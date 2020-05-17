from django.contrib import admin

from main.models import Ingredient, MyStoredIngredient


@admin.register(MyStoredIngredient)
class MyStoredIngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
