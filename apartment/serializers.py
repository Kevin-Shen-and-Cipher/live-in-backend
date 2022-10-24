from rest_framework import serializers
from job.serializers import DistrictSerializer
from .models import Apartment, Device, RentType, ApartmentType, Restrict, RoomType


class RentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentType
        fields = '__all__'


class ApartmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentType
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class RestrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restrict
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()
    rent_type = RentTypeSerializer()
    apartment_type = ApartmentTypeSerializer()
    room_type = RoomTypeSerializer()
    restrict = RestrictSerializer()
    device = DeviceSerializer()

    class Meta:
        model = Apartment
        fields = '__all__'
