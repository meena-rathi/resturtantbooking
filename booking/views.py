from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Hello, World!")
    return render(request, 'home.html')


def reservation(request):
    return render(request, 'reservation.html')

def menu(request):
    lunch_items = [
        {"image": "image/lunch1.webp", "description": "Pasta with vegetables and spicy sauces 10"},
        {"image": "image/lunch2.jpg", "description": "Pasta with vegetables and spicy sauces 10"},
        {"image": "image/lunch3.jpg", "description": "Pasta with vegetables and spicy sauces 10"},
        {"image": "image/lunch4.jpg", "description": "Pasta with vegetables and spicy sauces 10"},
    ]
    dinner_items = [
        {"image": "image/dinner1.jpg", "description": "Pasta with vegetables and spicy sauces 10"},
        {"image": "image/dinner2.webp", "description": "Pasta with vegetables and spicy sauces 10"},
        {"image": "image/dinner3.jpg", "description": "Pasta with vegetables and spicy sauces 10"},
        {"image": "image/dinner4.jpg", "description": "Pasta with vegetables and spicy sauces 10"},
    ]

    # Define dinner items


    context = {
        'lunch_items': lunch_items,
        'dinner_items': dinner_items,
   
    }
    return render(request, 'menu.html', context)