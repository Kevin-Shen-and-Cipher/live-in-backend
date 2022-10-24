from django.http import JsonResponse
from rest_framework.views import APIView
from algorithm.apartment_weight import ApartmentWeight
from .models import Apartment


class ApartmentView(APIView):
    
    def get(request):
        apartments = Apartment.objects.filter().values()
        address = request.GET.get("address")

        result = []
        if (address):
            result = ApartmentWeight().sort(list(apartments), address)

        return JsonResponse(result, safe=False)
