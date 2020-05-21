from django.http import HttpResponse
from django.shortcuts import render, redirect

from config.settings import SECRETS
from main.models import Ingredient, MyStoredIngredient, MyMemoIngredient


# sentry debug test
def trigger_error(request):
    division_by_zero = 1 / 0


# sentry CSP test web middleware
# type error (missing 1 required positional argument: 'response')
# def middleware(request, response):
#     response['Content-Security-Policy-Report-Only'] = \
#         "default-src 'self'; " \
#         f"report-uri {SECRETS['SENTRY_REPORT_URI']}"
#     return response


def main(request):
    return render(request, 'main/main.html')


def fridge(request):
    if request.user.is_authenticated:
        my_stored_ingredients = MyStoredIngredient.objects.filter(user=request.user)
        my_stored_ingredients_f, my_stored_ingredients_r, my_stored_ingredients_t = list(), list(), list()

        for my_stored_ingredient in my_stored_ingredients:
            if my_stored_ingredient.ingredient.fridger == 'F':
                my_stored_ingredients_f.append(my_stored_ingredient)
            elif my_stored_ingredient.ingredient.fridger == 'R':
                my_stored_ingredients_r.append(my_stored_ingredient)
            else:
                my_stored_ingredients_t.append(my_stored_ingredient)

        context = {
            'my_stored_ingredients': my_stored_ingredients,
            'my_stored_ingredients_f': my_stored_ingredients_f,
            'my_stored_ingredients_r': my_stored_ingredients_r,
            'my_stored_ingredients_t': my_stored_ingredients_t,
        }
        return render(request, 'main/fridge/fridge.html', context)
    return render(request, 'main/fridge/fridge.html')


def add_fridge(request):
    ingredients = Ingredient.objects.all().order_by('name')

    search_text = request.GET.get('search_text')

    if search_text:
        ingredients = ingredients.filter(name__contains=search_text)
    else:
        ingredients = ingredients

    context = {
        'ingredients': ingredients,
    }
    return render(request, 'main/fridge/add_fridge.html', context)


def input_date(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)

    if request.method == 'POST':
        if MyStoredIngredient.objects.filter(user=request.user, ingredient=ingredient):
            error_msg = '이미 추가되어 있는 재료입니다.'
            previous_btn = '이전으로'
            context = {
                'ingredient': ingredient,
                'error_msg': error_msg,
                'previous_btn': previous_btn,
            }
            return render(request, 'main/fridge/input_date.html', context)

        else:
            date = request.POST['input_date']
            MyStoredIngredient.objects.create(input_date=date, user=request.user, ingredient=ingredient)
            return redirect('main:fridge')

    else:
        context = {
            'ingredient': ingredient,
        }
        return render(request, 'main/fridge/input_date.html', context)


def delete_fridge_ingredient(request, pk):
    my_stored_ingredient = MyStoredIngredient.objects.get(pk=pk)
    my_stored_ingredient.delete()
    return redirect('main:fridge')


def add_vegetable(request):
    return render(request, 'main/fridge/type/vegetables.html')


def add_meat(request):
    return render(request, 'main/fridge/type/meat.html')


def add_marine(request):
    return render(request, 'main/fridge/type/marine.html')


def add_grain(request):
    return render(request, 'main/fridge/type/grain.html')


def add_sauce(request):
    return render(request, 'main/fridge/type/sauce.html')


def add_milk(request):
    return render(request, 'main/fridge/type/milk.html')


def add_others(request):
    return render(request, 'main/fridge/type/others.html')


def memo(request):
    if request.user.is_authenticated:
        my_memo_ingredients = MyMemoIngredient.objects.filter(user=request.user)
        ingredients_not_checked, ingredients_checked, my_memo_ingredients_ve, my_memo_ingredients_me, my_memo_ingredients_ma, my_memo_ingredients_gr, my_memo_ingredients_sa, my_memo_ingredients_mi, my_memo_ingredients_ot = list(), list(), list(), list(), list(), list(), list(), list(), list()

        for my_memo_ingredient in my_memo_ingredients:
            if my_memo_ingredient.status == 'not_checked':
                ingredients_not_checked.append(my_memo_ingredient)
            else:
                ingredients_checked.append(my_memo_ingredient)
            if my_memo_ingredient.ingredient is not None:
                if my_memo_ingredient.ingredient.type == 'vegetables':
                    my_memo_ingredients_ve.append(my_memo_ingredient)
                elif my_memo_ingredient.ingredient.type == 'meat':
                    my_memo_ingredients_me.append(my_memo_ingredient)
                elif my_memo_ingredient.ingredient.type == 'marine':
                    my_memo_ingredients_ma.append(my_memo_ingredient)
                elif my_memo_ingredient.ingredient.type == 'grain':
                    my_memo_ingredients_gr.append(my_memo_ingredient)
                elif my_memo_ingredient.ingredient.type == 'sauce':
                    my_memo_ingredients_sa.append(my_memo_ingredient)
                elif my_memo_ingredient.ingredient.type == 'milk':
                    my_memo_ingredients_mi.append(my_memo_ingredient)
                else:
                    my_memo_ingredients_ot.append(my_memo_ingredient)

        not_checked_count = len(ingredients_not_checked)
        checked_count = len(ingredients_checked)

        progress_percentage = int((checked_count / len(my_memo_ingredients)) * 100)
        print('progress_percentage >> ', progress_percentage)

        context = {
            'not_checked_count': not_checked_count,
            'progress_percentage': progress_percentage,
            'my_memo_ingredients': my_memo_ingredients,
            'my_memo_ingredients_ve': my_memo_ingredients_ve,
            'my_memo_ingredients_me': my_memo_ingredients_me,
            'my_memo_ingredients_ma': my_memo_ingredients_ma,
            'my_memo_ingredients_gr': my_memo_ingredients_gr,
            'my_memo_ingredients_sa': my_memo_ingredients_sa,
            'my_memo_ingredients_mi': my_memo_ingredients_mi,
        }
        return render(request, 'main/memo/memo.html', context)
    return render(request, 'main/memo/memo.html')


def add_memo(request):
    ingredients = Ingredient.objects.all().order_by('name')

    search_text = request.GET.get('search_text')

    if search_text:
        ingredients = ingredients.filter(name__contains=search_text)
    else:
        ingredients = ingredients

    context = {
        'ingredients': ingredients,
    }
    return render(request, 'main/memo/add_memo.html', context)


def add_memo_ingredient(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    MyMemoIngredient.objects.get_or_create(user=request.user, ingredient=ingredient)
    return redirect('main:memo')


def delete_memo_ingredient(request, pk):
    my_memo_ingredient = MyMemoIngredient.objects.get(pk=pk)
    my_memo_ingredient.delete()
    return redirect('main:memo')


def memo_check(request, pk):
    my_memo_ingredient = MyMemoIngredient.objects.get(pk=pk)
    if my_memo_ingredient.status == 'checked':
        my_memo_ingredient.status = 'not_checked'
        my_memo_ingredient.save()
    else:
        my_memo_ingredient.status = 'checked'
        my_memo_ingredient.save()
    return redirect('main:memo')


def memo_check_clear(request):
    my_memo_ingredients = MyMemoIngredient.objects.filter(user=request.user)
    for my_memo_ingredient in my_memo_ingredients:
        if my_memo_ingredient.status == 'checked':
            MyStoredIngredient.objects.get_or_create(user=request.user, ingredient=my_memo_ingredient.ingredient)
            my_memo_ingredient.delete()
            return redirect('main:memo')
        else:
            pass


def blog(request):
    return render(request, 'main/blog/blog.html')


def recommendation(request):
    return render(request, 'main/recommendation/recommendation.html')
