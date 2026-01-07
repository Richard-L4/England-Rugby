from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def tournament(request):
    return render(request, 'tournament.html')


def tournament_detail(request):
    return render(request, 'tournament-detail.html')


def about(request):
    return render(request, 'about.html')


def user_login(request):
    return render(request, 'login.html')


def user_logout(request):
    return render(request, 'logout.html')


def register(request):
    return render(request, 'register.html')


def confirm_logout(request):
    return render(request, 'confirm-logout.html')
