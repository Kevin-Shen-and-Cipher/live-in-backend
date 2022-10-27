from algorithm.job_weight import JobWeight
from django.http import HttpRequest, JsonResponse
from rest_framework import authentication, permissions, status
from rest_framework.views import APIView

from job.filters import JobFilter
from job.models import Job
from job.serializers import CreateJobSerializer, ListJobSerializer


class ListJobs(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        querys = self.request.GET

        # 過濾資料
        queryset = JobFilter.filter_all(
            querys, Job.objects.prefetch_related('benefit_set').all())

        return queryset

    def get(self, request: HttpRequest):
        result = []
        address = request.GET.get("address")

        if (address):
            data = self.get_queryset()
            serializer_data = ListJobSerializer(data, many=True).data
            result = JobWeight().sort(serializer_data, address)

        return JsonResponse(data=result, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request, *args, **kwargs):
        serializer = CreateJobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, json_dumps_params={'ensure_ascii': False}, status=status.HTTP_201_CREATED)

        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
