from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from members import apis

urlpatterns = [
    path('users/', apis.UserList.as_view()),
    path('users/<int:pk>/', apis.UserDetail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
