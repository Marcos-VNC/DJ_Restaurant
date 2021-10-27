from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cardapio', views.cardapio, name='cardapio'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('servicos', views.servicos, name='servicos'),
    path('logout', views.logout, name='logout'),

]