from django.urls import path

from job.views import ListJobs

urlpatterns = [
    path('api/jobs/', ListJobs.as_view()),
]
