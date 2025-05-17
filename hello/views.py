import os
from django.http import HttpResponse
from django.shortcuts import render

ENV = os.environ.get('ENV', 'dev')

def hello_world(request):
    return HttpResponse(f"<h1>Hello, World!</h1><p>Środowisko: {ENV}</p><p>Autor: Bartosz Bryniarski</p>")
