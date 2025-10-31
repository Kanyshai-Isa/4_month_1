from django.shortcuts import render, HttpResponse
from random import randint

# Create your views here.

def test_view(request):
    return HttpResponse(f"Рвндомное число: {randint(1,1000)}")

def html_view(request):
    return render(request, "base.html")
