#!/usr/bin/env python3

from urllib import request
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup

with open('crawling/crawling.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

food_lst = soup.select(
    '#content > div.contents_list_wrap.sub > ul.contents_list > li.contents_sub.active > ul > li > a')

NAMES, URLS, INGREDIENTS, RECIPES, TYPES, IMAGE_URLS = list(), list(), list(), list(), list(), list()
api = 'https://terms.naver.com'
for food in food_lst:
    url = api + food['href']
    food_name = food.next_element.next_element.next_element.next_element
    name = food_name.string.strip()

    NAMES.append(name)
    URLS.append(url)

# print('NAMES >> ', NAMES)
# print('URLS >> ', URLS)

not_none_i = list()
image_api = ''
for i, food_url in enumerate(URLS):
    path = f'/home/hyojinkwon/project-foodbox/app/crawling/recipe/{i}.html'

    with open(f'crawling/recipe/{i}.html') as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    food_ingredients = soup.select_one('div#size_ct > h3.stress').next_sibling.next_sibling
    not_none = list()
    for ingredient in food_ingredients:
        if ingredient.next_sibling is not None:
            not_none.append(i)
    if not_none:
        not_none_i.append(not_none[0])
    else:
        INGREDIENTS.append(ingredient)

    food_recipes = soup.select('div#size_ct > p.txt')
    food_recipe = list()
    for recipe in food_recipes:
        if recipe.string is not None:
            if recipe.string[1] == '.':
                food_recipe.append(recipe.string)
        else:
            pass
    RECIPES.append(food_recipe)

    if len(TYPES) == 56:
        pass
    else:
        if 0 <= i <= 2: TYPES.append('육수')
        if 3 <= i <= 18: TYPES.append('채소')
        if 19 <= i <= 24: TYPES.append('해산물')
        if 25 <= i <= 36: TYPES.append('고기/계란')
        if 37 <= i <= 43: TYPES.append('밥/쌀')
        if 44 <= i <= 51: TYPES.append('김치/발효')
        if 52 <= i <= 55: TYPES.append('간식/디저트')

    food_images = soup.select('div.thmb.c.thmb_border > span.img_box > a > img#innerImage0')
    for image in food_images:
        IMAGE_URLS.append(image['origin_src'])

for i, food_url in enumerate(IMAGE_URLS):
    # image_path = f'/home/hyojinkwon/project-foodbox/app/static/images/food/{i + 1}.jpg'
    # try:
    #     res = request.urlopen(food_url)
    #     contents = res.read()
    #     with open(image_path, 'wb') as c:
    #         c.write(contents)
    # except HTTPError as e:
    #     print('httperror occured!')
    # except URLError as e:
    #     print('urlerror occured!')
    # else:
    #     print('download succeed!')
    pass

# print('not_none_i >> ', not_none_i)
print(len(NAMES), len(URLS), len(INGREDIENTS), len(RECIPES), len(TYPES), len(IMAGE_URLS))

# print('INGREDIENTS >> ', INGREDIENTS)
# print('RECIPES >> ', RECIPES)
# print('TYPES >> ', TYPES)
