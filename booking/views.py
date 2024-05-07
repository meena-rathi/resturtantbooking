from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from .forms import ReservationsForm
from .models import Reservation
from datetime import date
from django.contrib import messages 
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


# Create your views here.
@login_required
def view_reservation(request):
    bookings = Reservation.objects.filter(user=request.user) 
    context = {"bookings": bookings}  
    return render(request, "view_reservation.html", context)


@login_required
def reservation(request):  
    if request.method == 'POST':
        form = ReservationsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            existing_reservation = Reservation.objects.filter(email=email).exists()
            if existing_reservation:
                return JsonResponse({'exists': True})  # Return JSON response indicating email exists
            else:
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                messages.success(request, 'Reservation successfully created.')
                return redirect('view_reservation') 
            
        else:
            messages.error(request, 'Form submission failed. Please check the errors.')
    else:
        initial_data = {'user': request.user} if request.user.is_authenticated else {}
        form = ReservationsForm(initial=initial_data)
    
    return render(request, 'reservation.html', {'form': form})
# def reservation(request):  
#     print("Inside reservation view")   
#     if request.method == 'POST':
#         form = ReservationsForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             existing_reservation = Reservation.objects.filter(email=email).exists()
#             if existing_reservation:
#                 # messages.error(request, 'You already have a reservation with this email.')
#                 return redirect('reservation')
#             else:
#                 reservation = form.save(commit=False)
#                 reservation.user = request.user
#                 reservation.save()
#                 messages.success(request, 'Reservation successfully created.')
#                 return redirect('view_reservation') 
#         else:
#             messages.error(request, 'Form submission failed. Please check the errors.')
#     else:
#         initial_data = {'user': request.user} if request.user.is_authenticated else {}
#         form = ReservationsForm(initial=initial_data)
#     return render(request, 'reservation.html', {'form': form})

def delete_booking(request, booking_id):
    reservation = get_object_or_404(Reservation, id=booking_id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('view_reservation') 
   
    
@login_required
def edit_reservation(request, booking_id):
    reservation = get_object_or_404(Reservation, id=booking_id)
    if request.method == 'POST':
        form = ReservationsForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('view_reservation')
    else:
        form = ReservationsForm(instance=reservation)
    return render(request, 'edit_reservation.html', {'form': form, 'booking': reservation})

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
        {"image": "image/lunch1.webp", "description": "Pasta with vegetables and spicy sauces 10"},
        {"image": "image/lunch2.jpg", "description": "Pasta with vegetables and spicy sauces 10"},
        {"image": "image/lunch3.jpg", "description": "Pasta with vegetables and spicy sauces 10"},
        {"image": "image/lunch4.jpg", "description": "Pasta with vegetables and spicy sauces 10"},
    ]

    # Define dinner items


    context = {
        'lunch_items': lunch_items,
        'dinner_items': dinner_items,
   
    }
    return render(request, 'menu.html', context)