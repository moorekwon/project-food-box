from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('fridge/', views.fridge, name='fridge'),
    path('fridge/add/', views.fridge_add, name='fridge-add'),
    path('fridge/add/<int:pk>/', views.add_ingredient, name='add-ingredient'),

    path('fridge/add/vegetables/', views.add_vegetable, name='add-vegetable'),
    path('fridge/add/meat/', views.add_meat, name='add-meat'),
    path('fridge/add/marine/', views.add_marine, name='add-marine'),
    path('fridge/add/grain/', views.add_grain, name='add-grain'),
    path('fridge/add/sauce/', views.add_sauce, name='add-sauce'),
    path('fridge/add/milk/', views.add_milk, name='add-milk'),
    path('fridge/add/others/', views.add_others, name='add-others'),

    path('memo/', views.memo, name='memo'),
    path('blog/', views.blog, name='blog'),
    path('recommendation/', views.recommendation, name='recommendation'),
]
