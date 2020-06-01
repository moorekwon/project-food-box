from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from crawling.crawling import NAMES, INGREDIENTS, RECIPES, TYPES, IMAGE_URLS
from main.models import Ingredient, RecommendedFood

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

        first = RecommendedFood.objects.filter(name=NAME[0])[0]
        second = RecommendedFood.objects.filter(name=NAME[1])[0]
        third = RecommendedFood.objects.filter(name=NAME[2])[0]
        fourth = RecommendedFood.objects.filter(name=NAME[3])[0]
        fifth = RecommendedFood.objects.filter(name=NAME[4])[0]
        sixth = RecommendedFood.objects.filter(name=NAME[5])[0]
        seventh = RecommendedFood.objects.filter(name=NAME[6])[0]
        eighth = RecommendedFood.objects.filter(name=NAME[7])[0]
        nineth = RecommendedFood.objects.filter(name=NAME[8])[0]
        tenth = RecommendedFood.objects.filter(name=NAME[9])[0]
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
