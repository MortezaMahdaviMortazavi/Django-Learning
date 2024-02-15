from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    # we can do these below:
    # pull data from db
    # Transform
    # Send email
    return render(request,'hello.html')