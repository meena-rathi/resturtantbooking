from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReservationsForm
from .models import Reservation
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    #return HttpResponse("Hello, World!")
    return render(request, 'home.html')


# Create your views here.
def view_reservation(request):
    bookings = Reservation.objects.all() 
    context = {"bookings": bookings}  
    return render(request, "view_reservation.html", context)
    
@login_required
def reservation(request):
    if request.method == 'POST':
        form = ReservationsForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  
            reservation.name = request.user.username  
            reservation.save()
            return redirect('view_reservation')
    else:
        initial_data = {'user': request.user.username} if request.user.is_authenticated else {}  
    context = {'form': form}
    return render(request, 'reservation.html', context)

def account(request):
    # Some logic here
    login_url = reverse('account_login')
    return HttpResponseRedirect(login_url)
         
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