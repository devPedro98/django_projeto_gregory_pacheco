from django.urls import path

from . import views

urlpatterns = [
    path('', views.listagem),
    path('home/', views.home),
    path('nova/', views.nova_transacao, name='url_nova'),
]
