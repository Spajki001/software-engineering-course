from django.contrib import admin
from django.urls import path, include

from images.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('images/', include('images.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
]
