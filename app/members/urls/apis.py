from django.urls import path

from members import apis

urlpatterns = [
    path('users/', apis.user_list),
    path('users/<int:pk>/', apis.user_detail),
]
