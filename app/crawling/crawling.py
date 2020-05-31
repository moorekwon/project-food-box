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
# print('soup >> ', soup)

food_lst = soup.select(
    '#content > div.contents_list_wrap.sub > ul.contents_list > li.contents_sub.active > ul > li > a')
# print('food_lst >> ', food_lst)

names, urls, ingredients, recipes = list(), list(), list(), list()
api = 'https://terms.naver.com'
for food in food_lst:
    # print('food >> ', food)
    url = api + food['href']
    food_name = food.next_element.next_element.next_element.next_element
    name = food_name.string.strip()

    names.append(name)
    urls.append(url)

# print('names >> ', names)
# print('urls >> ', urls)
print(len(names), len(urls))

path = '/home/hyojinkwon/project-foodbox/app/crawling/recipe/'
not_none_i = list()
for i, food_url in enumerate(urls):
    # print('food_url >> ', food_url)
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
    # print('food_ingredients >> ', food_ingredients)
    not_none = list()
    for ingredient in food_ingredients:
        # print('ingredient >> ', ingredient)
        if ingredient.next_sibling is not None:
            not_none.append(i)
    if not_none:
        not_none_i.append(not_none[0])
    else:
        ingredients.append(ingredient)

    food_recipes = soup.select('div#size_ct > p.txt')
    food_recipe = list()
    for recipe in food_recipes:
        if recipe.string is not None:
            if recipe.string[1] == '.':
                food_recipe.append(recipe.string)
        else:
            pass
    recipes.append(food_recipe)

# print('not_none_i >> ', not_none_i)
# print('ingredients >> ', ingredients)
# print('recipes >> ', recipes)
