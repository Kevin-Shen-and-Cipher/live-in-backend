from .views import ApartmentView
from django.urls import path

urlpatterns = [
    path('api/apartments/', ApartmentView.get),
]
