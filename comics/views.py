from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Series


def home(request):
    comics = Series.objects.all()
    return HttpResponse('Hello, World!')

