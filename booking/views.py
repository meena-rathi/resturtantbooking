from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Hello, World!")
    return render(request, 'home.html')


def reservation(request):
    return render(request, 'reservation.html')

def menu(request):
    return render(request, 'menu.html')