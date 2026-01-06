from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tournament/', views.tournament, name='tournament'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('tournament-detail/', views.tournament_detail,
         name='tournament-detail'),
    path('register/', views.register, name='register'),
    path('confirm-logout/', views.confirm_logout, name='confirm-logout'),
]
