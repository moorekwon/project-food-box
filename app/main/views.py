from django.shortcuts import render


def main(request):
    return render(request, 'main/main.html')


def fridge(request):
    return render(request, 'main/fridge.html')
