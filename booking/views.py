from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import ReservationsForm
from .models import Reservation
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


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
            existing_reservation = Reservation.objects.filter(
                email=email
            ).exists()
            if existing_reservation:
                messages.error(request, 'This email is already registered.')
                return JsonResponse({'exists': True})
            else:
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                messages.success(request, 'Reservation successfully created.')
                return JsonResponse({'success': True})
        else:
            messages.error(
                request, 'Form submission failed. Please check the errors.'
            )
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        initial_data = {
            'user': request.user
        } if request.user.is_authenticated else {}
        form = ReservationsForm(initial=initial_data)
    return render(request, 'reservation.html', {'form': form})


@login_required
def delete_booking(request, booking_id):
    reservation = get_object_or_404(Reservation, id=booking_id)
    if request.method == 'POST':
        reservation.delete()
        messages.success(
            request,
            'Booking has been deleted. We hope you will stay with us again!'
        )
        return redirect('view_reservation')
    else:
        messages.error(request, 'There was an error getting the booking.')
        return redirect('home')


@login_required
def edit_reservation(request, booking_id):
    reservation = get_object_or_404(Reservation, id=booking_id)
    if request.method == 'POST':
        form = ReservationsForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation successfully updated.')
            return redirect('view_reservation')
        else:
            messages.error(
                request, 'Form submission failed. Please check the errors.'
            )
    else:
        form = ReservationsForm(instance=reservation)
    return render(
        request,
        'edit_reservation.html',
        {'form': form, 'booking': reservation}
    )


def account(request):
    login_url = reverse('account_login')
    return HttpResponseRedirect(login_url)


def menu(request):
    lunch_items = [
        {
            "image": "image/lunch1.webp",
            "description": "Pasta with vegetables and spicy sauces $20"
        },
        {
            "image": "image/lunch2.jpg",
            "description": "Spicy Biryani with vegetables $20"
        },
        {
            "image": "image/lunch3.jpg",
            "description": "Cheese Paratha $15"
        },
        {
            "image": "image/lunch4.jpg",
            "description": "White rice with curry $20"
        },
        {
            "image": "image/lunch5.jpg",
            "description": "Sandwich $20"
        },
        {
            "image": "image/lunch6.jpg",
            "description": "Vegetable Thali $20"
        },
        {
            "image": "image/lunch7.jpg",
            "description": "Biryani $15"
        },
        {
            "image": "image/lunch8.jpg",
            "description": "Naan and paneer $20"
        },
    ]
    dinner_items = [
        {
            "image": "image/dinner1.jpg",
            "description": "Idli with chutney $20"
        },
        {
            "image": "image/dinner2.webp",
            "description": "Mix vegetables with rice $20"
        },
        {
            "image": "image/dinner3.jpg",
            "description": "Masala Dosa $10"
        },
        {
            "image": "image/dinner4.jpg",
            "description": "Naan Daal $20"
        },
        {
            "image": "image/dinner5.jpg",
            "description": "Vegetable rice $20"
        },
        {
            "image": "image/dinner6.jpg",
            "description": "Vegetable Pasta $20"
        },
        {
            "image": "image/dinner7.jpg",
            "description": "Biryani $15"
        },
        {
            "image": "image/dinner8.jpg",
            "description": "Rice"
        },
    ]
    drink_items = [
        {
            "image": "image/drink1.webp",
            "description": "Lemonade $5"
        },
        {
            "image": "image/drink2.webp",
            "description": "Margarita $5"
        },
        {
            "image": "image/drink3.jpg",
            "description": "Masala Dosa $10"
        },
        {
            "image": "image/drink4.jpg",
            "description": "Wine $8"
        },
        {
            "image": "image/drink5.jpg",
            "description": "Aperol Spritz $5"
        },
        {
            "image": "image/drink6.jpg",
            "description": "Mojito $4"
        },
        {
            "image": "image/drink4.jpg",
            "description": "Water $5"
        },
        {
            "image": "image/drink2.webp",
            "description": "Mojito $4"
        },
    ]

    context = {
        'lunch_items': lunch_items,
        'dinner_items': dinner_items,
        'drink_items': drink_items,
    }
    return render(request, 'menu.html', context)
