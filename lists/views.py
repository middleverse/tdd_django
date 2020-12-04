from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home_page(request):
    return HttpResponse('<html><title>TODO Lists</title></html>')
