from django.urls import path

from . import views

urlpatterns = [
    path('', views.listagem),
    path('home/', views.home),
    path('create/', views.nova_transacao, name='url_create'),
    path('update/<int:pk>/', views.update, name='url_update'),
    path('delete/<int:pk>/', views.delete, name='url_delete'),
]
