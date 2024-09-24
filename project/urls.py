
from django.contrib import admin
from django.urls import path
from etmad.views import scraped_data_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scraped_data_view, name='scraped_data'),
]
