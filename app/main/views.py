from django.shortcuts import render

from main.models import Ingredient


def main(request):
    return render(request, 'main/main.html')


def fridge(request):
    if request.user.is_authenticated:
        ingredients = Ingredient.objects.filter(user=request.user)

        context = {
            'ingredients': ingredients,
        }
        return render(request, 'main/fridge/fridge.html', context)


def add_ingredient(request):
    return render(request, 'main/fridge/ingredients.html')


def add_vegetable(request):
    return render(request, 'main/fridge/vegetables.html')


def add_meat(request):
    return render(request, 'main/fridge/meat.html')


def add_marine(request):
    return render(request, 'main/fridge/marine.html')


def add_grain(request):
    return render(request, 'main/fridge/grain.html')


def add_sauce(request):
    return render(request, 'main/fridge/sauce.html')


def add_milk(request):
    return render(request, 'main/fridge/milk.html')


def add_others(request):
    return render(request, 'main/fridge/others.html')


def memo(request):
    return render(request, 'main/memo.html')


def menu(request):
    return render(request, 'main/menu.html')


def recommendation(request):
    return render(request, 'main/recommendation.html')
