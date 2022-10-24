from .views import JobView
from django.urls import path

urlpatterns = [
    path('api/jobs/', JobView.get),
]
