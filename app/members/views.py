from django.shortcuts import render


def signin(request):
    return render(request, 'members/signin.html')


def signup(request):
    return render(request, 'members/signup.html')
