from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shuffle', include('shuffleapp.urls')),
    path('pesel', include('pesel.urls')),
]
