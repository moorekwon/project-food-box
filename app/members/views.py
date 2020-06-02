from django.contrib.auth import authenticate, login, get_user_model, logout
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

User = get_user_model()


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
    if request.method == 'POST':
        email = request.POST['email']
        nickname = request.POST['nickname']
        birth = request.POST['birth']
        password = request.POST['password']
        users = User.objects.all()

        if users.filter(email=email):
            error_msg = '이미 사용중인 email 입니다.'
            context = {
                'error_msg': error_msg,
            }
            return render(request, 'members/signup.html', context)
        if users.filter(nickname=nickname):
            error_msg = '이미 사용중인 nickname 입니다.'
            context = {
                'error_msg': error_msg,
            }
            return render(request, 'members/signup.html', context)

        user = User.objects.create_user(email=email, nickname=nickname, birth=birth, password=password)
        login(request, user)
        return redirect('main:fridge')
    return render(request, 'members/signup.html')


def logoff(request):
    logout(request)
    return redirect('start')
