from django.contrib import admin
from django.urls import path, include
from django.urls import reverse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resturtant.urls')),
    #path('accounts/', include('allauth.urls')),
    path("accounts/", include("allauth.urls")),
]