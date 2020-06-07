from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('fridge/', views.fridge, name='fridge'),
    path('fridge/add/', views.add_fridge, name='add-fridge'),
    path('fridge/add/<int:pk>/', views.input_date, name='input-date'),

    path('fridge/add/vegetables/', views.add_vegetable, name='add-vegetable'),
    path('fridge/add/meat/', views.add_meat, name='add-meat'),
    path('fridge/add/marine/', views.add_marine, name='add-marine'),
    path('fridge/add/grain/', views.add_grain, name='add-grain'),
    path('fridge/add/sauce/', views.add_sauce, name='add-sauce'),
    path('fridge/add/milk/', views.add_milk, name='add-milk'),
    path('fridge/add/others/', views.add_others, name='add-others'),

    path('fridge/delete/<int:pk>/', views.delete_fridge_ingredient, name='delete-fridge-ingredient'),

    path('memo/', views.memo, name='memo'),
    path('memo/add/', views.add_memo, name='add-memo'),
    path('memo/add/<int:pk>/', views.add_memo_ingredient, name='add-memo-ingredient'),
    path('memo/delete/<int:pk>/', views.delete_memo_ingredient, name='delete-memo-ingredient'),
    path('memo/check/<int:pk>/', views.memo_check, name='memo-check'),
    path('memo/check/clear/', views.memo_check_clear, name='memo-check-clear'),

    path('recommendation/', views.recommendation, name='recommendation'),
    path('recommendation/recipe/<int:pk>/', views.recipe, name='recipe'),
    path('recommendation/like/<int:pk>/', views.like, name='like'),

    path('store/', views.store, name='store'),
]
