"""
URL configuration for resturtant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking.views import home, reservation, menu,view_reservation, delete_booking,edit_reservation,delete_booking

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('reservation/', reservation, name='reservation'),
    path('menu/', menu, name='menu'),
    path('view_reservation/', view_reservation, name='view_reservation'),
    path("accounts/", include("allauth.urls")),

    path('delete_booking/<int:booking_id>/', delete_booking, name='delete_booking'),
    path('edit_reservation/<int:booking_id>/', edit_reservation, name='edit_reservation'),
]
