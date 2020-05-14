from django.shortcuts import render


def main(request):
    return render(request, 'main/main.html')


def fridge(request):
    return render(request, 'main/fridge.html')


def memo(request):
    return render(request, 'main/memo.html')


def menu(request):
    return render(request, 'main/menu.html')


def recommendation(request):
    return render(request, 'main/recommendation.html')
