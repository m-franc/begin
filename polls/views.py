from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("J'ai commencé Django héhéhé")