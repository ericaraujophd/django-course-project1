from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HTTP Response
    return HttpResponse("Home")


def sobre(request):
    # return HTTP Response
    return HttpResponse("Sobre")


def contato(request):
    # return HTTP Response
    return HttpResponse("Contato")
