from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

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

        print('Ingredient.objects.all() >> ', Ingredient.objects.all())
        print('Ingredient 객체들이 성공적으로 생성되었습니다.')

        apple = Ingredient.objects.get(name=NAME[0])
        blueberry = Ingredient.objects.get(name=NAME[1])
        mackerel = Ingredient.objects.get(name=NAME[2])
        lemon = Ingredient.objects.get(name=NAME[3])
        print('Ingredient 객체들에게 각각 변수명을 할당하였습니다.')

        # hjk = User.objects.get(email='hjk@hjk.com')
        # print('User 객체에 변수명을 할당하였습니다.')

        NAME = ('불고기', '쌈밥', '고등어조림')
        DETAIL = (
            '소고기 600g, 느타리버섯 120g, 팽이버섯 80g, 양파 1개, 대파 ½개, 식용유 2큰술',
            '쌈 채소 200g, 양배추 200g, 당근 1개, 오이 1개, 밥 4컵',
            '멸치 육수 2컵, 무 250g, 양파 ½개, 대파 ½개'
        )
        RECIPE = (
            '<p class="txt">1. 양념장을 먼저 만든 후 준비된 소고기에 넣고 냉장고에서 3시간 숙성시킨다.</p> <p class="txt">2. 버섯은 비슷한 크기로 다듬는다. 양파는 채 썰고 대파는 어슷 썬다.</p> <p class="txt">3. 달군 팬에 기름을 두른 후 양파와 불고기를 넣고 센 불에서 볶는다.</p> <p class="txt">4. 불고기가 반쯤 익었을 때 버섯을 넣고 볶는다.</p>',
            '<p class="txt">1. 쌈장을 만든다.</p> <p class="txt">2. 쌈 채소는 잘 씻어 물기를 제거하고, 양배추는 크게 잘라 찜통에 15분간 쪄서 익힌다.</p> <p class="txt">3. 당근과 오이를 길게 잘라 쌈장에 찍어 먹을 수 있게 준비한다.</p> <p class="txt">4. 쌈장과 채소를 밥과 함께 상에 낸다.</p>',
            '<h3 class="stress" id="TABLE_OF_CONTENT3">조리순서</h3> <p class="txt">1. 고등어의 내장과 지느러미를 제거한 뒤 찬물에 헹군다. 무와 양파는 1.5cm 두께로 썰고 대파는 어슷 썬다.</p> <p class="txt">2. 그릇에 양념장 재료를 넣고 잘 섞는다.</p> <p class="txt">3. 냄비에 무와 양파를 넣고 그 위에 고등어를 올린다.</p> <p class="txt">4. 양념장을 고등어 위에 끼얹고 멸치육수를 붓는다.</p> <p class="txt">5. 센 불에서 끓기 시작하면 약한 불로 줄여 무와 고등어가 완전히 익을 때까지 조린다.</p> <p class="txt">6. 마지막에 어슷 썬 대파를 얹는다.</p>'
        )
        TYPE = ('고기/계란', '채소', '해산물')

        name_count = len(NAME)
        for index in range(name_count):
            RecommendedFood.objects.get_or_create(name=NAME[index], ingredients_detail=DETAIL[index],
                                                  recipe=RECIPE[index],
                                                  type=TYPE[index])
        print('RecommendedFood.objects.all() >> ', RecommendedFood.objects.all())
        print('RecommendedFood 객체들이 성공적으로 생성되었습니다.')

        bulgogi = RecommendedFood.objects.get(name=NAME[0])
        ssambab = RecommendedFood.objects.get(name=NAME[1])
        braised_mac = RecommendedFood.objects.get(name=NAME[2])

        print('RecommendedFood 객체들에게 각각 변수명을 할당하였습니다.')

        bulgogi.ingredient.add(lemon)
        bulgogi.ingredient.add(apple)
        ssambab.ingredient.add(blueberry)
        ssambab.ingredient.add(apple)
        braised_mac.ingredient.add(mackerel)
        print('RecommendedFood 객체들에게 각각 Ingredient 객체들을 추가하였습니다.')
