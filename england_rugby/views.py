from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def tournament(request):
    return render(request, 'tournament.html')
