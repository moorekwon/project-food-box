from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from members import apis

urlpatterns = [
    path('users/', apis.user_list),
    path('users/<int:pk>/', apis.user_detail),
]

urlpatterns += format_suffix_patterns(urlpatterns)
