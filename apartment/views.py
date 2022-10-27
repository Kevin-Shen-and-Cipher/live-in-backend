from algorithm.apartment_weight import ApartmentWeight
from django.http import HttpRequest, JsonResponse
from rest_framework import authentication, permissions, status
from rest_framework.views import APIView

from apartment.filters import ApartmentFilter
from apartment.models import Apartment
from apartment.serializers import (CreateApartmentSerializer,
                                   ListApartmentSerializer)


class ListApartments(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        querys = self.request.GET

        # 過濾資料
        queryset = ApartmentFilter.filter_all(
            querys, Apartment.objects.prefetch_related('surroundingfacility_set').all())

        return queryset

    def get(self, request: HttpRequest):
        result = []
        address = request.GET.get("address")

        if (address):
            data = self.get_queryset()
            serializer_data = ListApartmentSerializer(data, many=True).data
            result = ApartmentWeight().sort(serializer_data, address)

        return JsonResponse(data=result, safe=False, json_dumps_params={'ensure_ascii': False})

    def post(self, request, *args, **kwargs):
        serializer = CreateApartmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, json_dumps_params={'ensure_ascii': False}, status=status.HTTP_201_CREATED)

        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
