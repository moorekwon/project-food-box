from django.shortcuts import render

from members.forms import UserForm


def signin(request):
    form = UserForm()
    return render(request, 'members/signin.html', {'form': form})
