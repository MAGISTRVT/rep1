from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет малыш я Ёжик!")


def test(request):
    return HttpResponse("Капелька, капелька, капелка дождя!")
