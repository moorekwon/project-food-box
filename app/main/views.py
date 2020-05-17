from django.shortcuts import render, redirect

from main.models import Ingredient, MyStoredIngredient


def main(request):
    return render(request, 'main/main.html')


def fridge(request):
    if request.user.is_authenticated:
        my_stored_ingredients = MyStoredIngredient.objects.filter(user=request.user)

        context = {
            'my_stored_ingredients': my_stored_ingredients,
        }
        return render(request, 'main/fridge/fridge.html', context)
    return render(request, 'main/fridge/fridge.html')


def fridge_add(request):
    ingredients = Ingredient.objects.all().order_by('name')

    search_text = request.GET.get('search_text')

    if search_text:
        ingredients = ingredients.filter(name__contains=search_text)
    else:
        ingredients = ingredients

    context = {
        'ingredients': ingredients,
    }
    return render(request, 'main/fridge/fridge_add.html', context)


def add_ingredient(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)

    if request.method == 'POST':
        if MyStoredIngredient.objects.filter(user=request.user, ingredient=ingredient):
            error_msg = '이미 추가되어 있는 재료입니다.'
            context = {
                'ingredient': ingredient,
                'error_msg': error_msg,
            }
            return render(request, 'main/fridge/add_ingredient.html', context)

        else:
            date = request.POST['input_date']
            MyStoredIngredient.objects.create(input_date=date, user=request.user, ingredient=ingredient)
            return redirect('main:fridge')

    else:
        context = {
            'ingredient': ingredient,
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
    return render(request, 'main/memo/memo.html')


def blog(request):
    return render(request, 'main/blog/blog.html')


def recommendation(request):
    return render(request, 'main/recommendation/recommendation.html')
