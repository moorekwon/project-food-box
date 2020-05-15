from django.contrib import admin

from main.models import Ingredient, IngredientInfo


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(IngredientInfo)
class IngredientInfoAdmin(admin.ModelAdmin):
    pass
