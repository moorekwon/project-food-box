from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect('main:fridge')
        if ValidationError:
            error_msg = 'Email 혹은 Password가 틀립니다.'
            context = {
                'error_msg': error_msg,
            }
            return render(request, 'members/signin.html', context)
    return render(request, 'members/signin.html')


def signup(request):
    return render(request, 'members/signup.html')
