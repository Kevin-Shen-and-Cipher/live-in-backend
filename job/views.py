from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from algorithm.job_weight import JobWeight
from .models import Job


class JobView(GenericAPIView):

    def get(request):
        jobs = Job.objects.filter().values()

        address = request.GET.get("address")

        result = []
        if (address):
            result = JobWeight().sort(list(jobs), address)

        return JsonResponse(result, safe=False)
