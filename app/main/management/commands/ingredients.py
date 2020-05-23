from django.core.management import BaseCommand

from main.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        NAME = ('사과', '블루베리', '고등어', '레몬')
        KEEPING_DAYS = (4, 30, 100, 7)
        KCALORIES = (300, 200, 400, 250)
        TYPE = ('vegetables', 'vegetables', 'marine', 'vegetables')
        FRIDGER = ('R', 'F', 'F', 'R')
        IMAGES = ('사과.png', '블루베리.jpg', '고등어.jpg', '레몬.jpg')

        count = len(NAME)

        for index in range(count):
            Ingredient.objects.get_or_create(name=NAME[index], keeping_days=KEEPING_DAYS[index],
                                             kcalories=KCALORIES[index], type=TYPE[index], fridger=FRIDGER[index],
                                             image=f'images/ingredients/{IMAGES[index]}')

        print('Ingredient.objects.all() >> ', Ingredient.objects.all())
