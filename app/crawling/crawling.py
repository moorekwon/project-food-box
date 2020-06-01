#!/usr/bin/env python3

from urllib import request
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup

# path = '/home/hyojinkwon/project-foodbox/app/crawling/crawling.html'
# url = 'https://terms.naver.com/list.nhn?cid=42701&categoryId=62905'
#
# try:
#     res = request.urlopen(url)
#     contents = res.read()
#
#     with open(path, 'wb') as c:
#         c.write(contents)
# except HTTPError as e:
#     print('httperror occured!')
# except URLError as e:
#     print('urlerror occured!')
# else:
#     print('download succeed!')

with open('crawling/crawling.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

food_lst = soup.select(
    '#content > div.contents_list_wrap.sub > ul.contents_list > li.contents_sub.active > ul > li > a')

NAMES, URLS, INGREDIENTS, RECIPES, TYPES = list(), list(), list(), list(), list()
api = 'https://terms.naver.com'
for food in food_lst:
    url = api + food['href']
    food_name = food.next_element.next_element.next_element.next_element
    name = food_name.string.strip()

    NAMES.append(name)
    URLS.append(url)

# print('NAMES >> ', NAMES)
# print('URLS >> ', URLS)

path = '/home/hyojinkwon/project-foodbox/app/crawling/recipe/'
not_none_i = list()
for i, food_url in enumerate(URLS):
    path = f'/home/hyojinkwon/project-foodbox/app/crawling/recipe/{i}.html'

    # try:
    #     res = request.urlopen(food_url)
    #     contents = res.read()
    #
    #     with open(path, 'wb') as c:
    #         c.write(contents)
    # except HTTPError as e:
    #     print('httperror occured!')
    # except URLError as e:
    #     print('urlerror occured!')
    # else:
    #     print('download succeed!')

    # print('path >> ', path)
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

    if i >= 0 and i <= 2: TYPES.append('육수')
    if i >= 3 and i <= 18: TYPES.append('채소')
    if i >= 19 and i <= 24: TYPES.append('해산물')
    if i >= 25 and i <= 36: TYPES.append('고기/계란')
    if i >= 37 and i <= 43: TYPES.append('밥/쌀')
    if i >= 44 and i <= 51: TYPES.append('김치/발효')
    if i >= 52 and i <= 55: TYPES.append('간식/디저트')

# print('not_none_i >> ', not_none_i)

# print('INGREDIENTS >> ', INGREDIENTS)
# print('RECIPES >> ', RECIPES)
# print('TYPES >> ', TYPES)

# print(len(NAMES), len(URLS), len(INGREDIENTS), len(RECIPES), len(TYPES))
