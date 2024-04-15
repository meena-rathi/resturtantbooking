from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReservationsForm
from .models import Reservation

# Create your views here.
def home(request):
    #return HttpResponse("Hello, World!")
    return render(request, 'home.html')


# Create your views here.
def view_reservation(request):
    bookings = Reservation.objects.all() 
    context = {"bookings": bookings}  
    return render(request, "view_reservation.html", context)

def reservation(request):
    try:
        if request.method == 'POST':
            form = ReservationsForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)  # Check the form data in console
                form.save()
            else:
                print(form.errors)  # Print form errors
        else:
            form = ReservationsForm()
        context = {'form': form}
        return render(request, 'reservation.html', context)
    except Exception as e:
        print(e)  # Print any exception that occurs

        
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