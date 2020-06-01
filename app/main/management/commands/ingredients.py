from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from crawling.crawling import NAMES, INGREDIENTS, RECIPES, TYPES
from main.models import Ingredient, RecommendedFood, MyStoredIngredient

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        NAME = ('사과', '블루베리', '고등어', '레몬')
        KEEPING_DAYS = (4, 30, 100, 7)
        KCALORIES = (300, 200, 400, 250)
        TYPE = ('vegetables', 'vegetables', 'marine', 'vegetables')
        FRIDGER = ('R', 'F', 'F', 'R')
        IMAGES = ('사과.png', '블루베리.jpg', '고등어.jpg', '레몬.jpg')
        name_count = len(NAME)

        for index in range(name_count):
            Ingredient.objects.get_or_create(name=NAME[index], keeping_days=KEEPING_DAYS[index],
                                             kcalories=KCALORIES[index], type=TYPE[index], fridger=FRIDGER[index],
                                             image=f'images/ingredients/{IMAGES[index]}')
        print('Ingredient 객체들이 성공적으로 생성되었습니다.')

        apple = Ingredient.objects.get(name=NAME[0])
        blueberry = Ingredient.objects.get(name=NAME[1])
        mackerel = Ingredient.objects.get(name=NAME[2])
        lemon = Ingredient.objects.get(name=NAME[3])
        print('Ingredient 객체들에게 각각 변수명을 할당하였습니다.')

        NAME = NAMES
        DETAIL = INGREDIENTS
        RECIPE = RECIPES
        TYPE = TYPES

        name_count = len(NAME)
        for index in range(name_count):
            RecommendedFood.objects.get_or_create(name=NAME[index], ingredients_detail=DETAIL[index],
                                                  recipe=RECIPE[index], type=TYPE[index])
        print('RecommendedFood 객체들이 성공적으로 생성되었습니다.')

        first = RecommendedFood.objects.get(name=NAME[50])
        second = RecommendedFood.objects.get(name=NAME[51])
        third = RecommendedFood.objects.get(name=NAME[52])
        fourth = RecommendedFood.objects.get(name=NAME[53])
        fifth = RecommendedFood.objects.get(name=NAME[54])
        sixth = RecommendedFood.objects.get(name=NAME[55])
        seventh = RecommendedFood.objects.get(name=NAME[46])
        eighth = RecommendedFood.objects.get(name=NAME[47])
        nineth = RecommendedFood.objects.get(name=NAME[48])
        tenth = RecommendedFood.objects.get(name=NAME[49])
        print('RecommendedFood 객체들에게 각각 변수명을 할당하였습니다.')

        first.ingredient.add(lemon)
        first.ingredient.add(apple)
        second.ingredient.add(blueberry)
        third.ingredient.add(apple)
        fourth.ingredient.add(mackerel)
        fifth.ingredient.add(blueberry)
        sixth.ingredient.add(lemon)
        seventh.ingredient.add(blueberry)
        eighth.ingredient.add(lemon)
        nineth.ingredient.add(mackerel)
        tenth.ingredient.add(mackerel)
        print('RecommendedFood 객체들에게 각각 Ingredient 객체들을 추가하였습니다.')

        hjk = User.objects.get(email='hjk@hjk.com')
        MyStoredIngredient.objects.get_or_create(user=hjk, ingredient=lemon)
        MyStoredIngredient.objects.get_or_create(user=hjk, ingredient=blueberry)
        MyStoredIngredient.objects.get_or_create(user=hjk, ingredient=mackerel)
        MyStoredIngredient.objects.get_or_create(user=hjk, ingredient=apple)
        print('user가 hjk인 MyStoredIngredient 객체들을 추가하였습니다.')
