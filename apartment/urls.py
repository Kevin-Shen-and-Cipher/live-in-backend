from django.urls import path

from apartment.views import ListApartments

urlpatterns = [
    path('api/apartments/', ListApartments.as_view()),
]
