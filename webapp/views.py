from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template("webapp/index.html")
    return HttpResponse(template.render(request=request))


def results(request):
    template = loader.get_template("webapp/results.html")
    return HttpResponse(template.render(request=request))
