from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def landingPAge(request):
    # return HttpResponse('hello world')
    return render(request, 'home.html')