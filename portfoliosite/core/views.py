from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def index(request):
    # return HttpResponse(f"Hello world. you are at my portfolio website.{datetime.datetime.now()}" )
    context = {}
    return render(request, 'projectslisting.html', context)