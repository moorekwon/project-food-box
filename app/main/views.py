from django.shortcuts import render, redirect

from main.models import Ingredient, MyStoredIngredient, MyMemoIngredient, RecommendedFood


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


def start(request):
    return render(request, 'start.html')


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

    if search_text != '' and search_text is not None:
        ingredients = ingredients.filter(name__contains=search_text)

    context = {
        'ingredients': ingredients,
    }
    return render(request, 'main/fridge/add_fridge.html', context)


def input_date(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    print('ingredient.image.url >> ', ingredient.image.url)

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

        date = request.POST['input_date']
        MyStoredIngredient.objects.create(input_date=date, user=request.user, ingredient=ingredient)
        return redirect('main:fridge')

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
        all_count = len(my_memo_ingredients)

        if all_count:
            progress_percentage = int((checked_count / all_count) * 100)
        else:
            progress_percentage = 0

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
    return redirect('main:memo')


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
    checked_clear = list()
    for my_memo_ingredient in my_memo_ingredients:
        if my_memo_ingredient.status == 'checked':
            MyStoredIngredient.objects.get_or_create(user=request.user, ingredient=my_memo_ingredient.ingredient)
            checked_clear.append(my_memo_ingredient)
        else:
            pass

    for checked_clear_item in checked_clear:
        checked_clear_item.delete()
    return redirect('main:memo')


def recommendation(request):
    if request.user.is_authenticated:
        my_stored_ingredients = MyStoredIngredient.objects.filter(user=request.user)

        food_all, food_br, food_ve, food_ma, food_me, food_ri, food_ki, food_de = list(), list(), list(), list(), list(), list(), list(), list()
        for my_stored_ingredient in my_stored_ingredients:
            all_food = RecommendedFood.objects.filter(ingredient=my_stored_ingredient.ingredient)

            for food in all_food:
                if food is not None:
                    if food.type == '육수':
                        food_br.append(food)
                    elif food.type == '채소':
                        food_ve.append(food)
                    elif food.type == '해산물':
                        food_ma.append(food)
                    elif food.type == '고기/계란':
                        food_me.append(food)
                    elif food.type == '쌀/밥':
                        food_ri.append(food)
                    elif food.type == '김치/발효':
                        food_ki.append(food)
                    elif food.type == '간식/디저트':
                        food_de.append(food)

        food_all = food_br + food_ve + food_ma + food_me + food_ri + food_ki + food_de

        context = {
            'food_all_set': set(food_all),
            'food_br_set': set(food_br),
            'food_ve_set': set(food_ve),
            'food_ma_set': set(food_ma),
            'food_me_set': set(food_me),
            'food_ri_set': set(food_ri),
            'food_ki_set': set(food_ki),
            'food_de_set': set(food_de),
        }
        return render(request, 'main/recommendation/recommendation.html', context)
    return redirect('main:recommendation')


def like(request, pk):
    recommended_food = RecommendedFood.objects.get(pk=pk)
    if request.user in recommended_food.user.all():
        recommended_food.user.remove(request.user)
    else:
        recommended_food.user.add(request.user)
    return redirect('main:recommendation')


def recipe(request, pk):
    food = RecommendedFood.objects.get(pk=pk)
    food_ingredients = food.ingredients_detail.split(',')
    food_recipe = eval('' + food.recipe + '')

    comments = food.foodcomment_set.all()

    context = {
        'food': food,
        'food_ingredients': food_ingredients,
        'food_recipe': food_recipe,
        'comments': comments,
    }
    return render(request, 'main/recommendation/recipe.html', context)


def comment_create(request, pk):
    if request.method == 'POST':
        food = RecommendedFood.objects.get(pk=pk)
        user = request.user
        comment = request.POST['input_comment']
        food.foodcomment_set.create(user=user, comment=comment)

        return redirect('main:recipe', pk=food.pk)


def store(request):
    return render(request, 'main/store/store.html')
