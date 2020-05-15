from django.shortcuts import render, redirect

from main.models import Ingredient, IngredientInfo


def main(request):
    return render(request, 'main/main.html')


def fridge(request):
    if request.user.is_authenticated:
        ingredients = Ingredient.objects.filter(user=request.user)

        context = {
            'ingredients': ingredients,
        }
        return render(request, 'main/fridge/fridge.html', context)
    return render(request, 'main/fridge/fridge.html')


def fridge_add(request):
    ingredient_infos = IngredientInfo.objects.all().order_by('name')

    search_text = request.GET.get('search_text')

    if search_text:
        ingredient_infos = ingredient_infos.filter(name__contains=search_text)
    else:
        ingredient_infos = ingredient_infos

    context = {
        'ingredient_infos': ingredient_infos,
    }
    return render(request, 'main/fridge/fridge_add.html', context)


def add_ingredient(request, pk):
    ingredient_info = IngredientInfo.objects.get(pk=pk)

    if request.method == 'POST':
        date = request.POST['input_date']

        Ingredient.objects.create(input_date=date, user=request.user, info=ingredient_info)
        return redirect('main:fridge')

    else:
        context = {
            'ingredient_info': ingredient_info,
        }
        return render(request, 'main/fridge/add_ingredient.html', context)


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
