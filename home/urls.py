from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('cardapio', views.cardapio, name='cardapio'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('servicos', views.servicos, name='servicos'),
    path('logout', views.logout, name='logout'),
    path("api/", LancheAPIView.as_view(), name='api_lanche'),
    path('api/<int:pk>', LancheAPIView.as_view(), name='api_lanche_parameters'),

]