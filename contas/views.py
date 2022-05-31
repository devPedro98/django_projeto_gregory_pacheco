from django.shortcuts import render


def home(request):
    return render(request, 'contas/html/home.html')
