from django.urls import path

from members import views

app_name = 'members'
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]
