from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Greetings, Son of Mogh. Your house is honorable, and I pledge myself to your service!")