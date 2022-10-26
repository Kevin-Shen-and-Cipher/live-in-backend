from job.serializers import DistrictSerializer
from rest_framework import serializers

from apartment.models import (Apartment, ApartmentType, Device, RentType,
                              Restrict, RoomType, SurroundingFacility)


class RentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentType
        fields = ['name']


class ApartmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentType
        fields = ['name']


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['name']


class RestrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restrict
        fields = ['name']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name']


class SurroundingFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SurroundingFacility
        fields = ['name']


class ApartmentSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()
    rent_type = RentTypeSerializer()
    apartment_type = ApartmentTypeSerializer()
    room_type = RoomTypeSerializer()
    restrict = RestrictSerializer(many=True, read_only=True)
    device = DeviceSerializer(many=True, read_only=True)
    surroundingfacility_set = SurroundingFacilitySerializer(
        many=True, read_only=True)

    class Meta:
        model = Apartment
        exclude = ['id', 'created_at', 'updated_at']
        depth = 1
