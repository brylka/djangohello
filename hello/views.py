from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1><p>Autor: Bartosz Bryniarski</p>")
