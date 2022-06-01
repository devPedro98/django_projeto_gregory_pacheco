from django.urls import path

from . import views

urlpatterns = [
    path('', views.listagem),
    path('home/', views.home),
]
