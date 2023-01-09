from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main/home.html')


def demand(request):
    return render(request, 'main/demand.html')


def geography(request):
    return render(request, 'main/geography.html')


def skills(request):
    return render(request, 'main/skills.html')
