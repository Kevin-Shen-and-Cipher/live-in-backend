from job.models import District
from job.serializers import DistrictSerializer
from rest_framework import serializers

from apartment.models import (Apartment, ApartmentType, Device, FacilityType,
                              RentType, Restrict, RoomType,
                              SurroundingFacility)


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

class FacilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityType
        fields = ['name']

class SurroundingFacilitySerializer(serializers.ModelSerializer):
    facility_type = FacilityTypeSerializer(read_only=True)
    
    class Meta:
        model = SurroundingFacility
        fields = ['name','facility_type']


class ListApartmentSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)

    rent_type = RentTypeSerializer(read_only=True)

    apartment_type = ApartmentTypeSerializer(read_only=True)

    room_type = RoomTypeSerializer(read_only=True)

    restrict = RestrictSerializer(
        many=True,
        read_only=True)

    device = DeviceSerializer(
        many=True,
        read_only=True)

    surroundingfacility = SurroundingFacilitySerializer(
        source='surroundingfacility_set',
        many=True,
        read_only=True)

    class Meta:
        model = Apartment
        exclude = ['id', 'created_at', 'updated_at']


class CreateSurroundingFacilitySerializer(serializers.ModelSerializer):
    facility_type = serializers.PrimaryKeyRelatedField(
        queryset=FacilityType.objects.all())

    class Meta:
        model = SurroundingFacility
        fields = ['name', 'facility_type']


class CreateApartmentSerializer(serializers.ModelSerializer):
    district = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all(),
        write_only=True)

    rent_type = serializers.PrimaryKeyRelatedField(
        queryset=RentType.objects.all(),
        write_only=True)

    apartment_type = serializers.PrimaryKeyRelatedField(
        queryset=ApartmentType.objects.all(),
        write_only=True)

    room_type = serializers.PrimaryKeyRelatedField(
        queryset=RoomType.objects.all(),
        write_only=True)

    restrict = serializers.PrimaryKeyRelatedField(
        queryset=Restrict.objects.all(),
        many=True,
        write_only=True,
        allow_null=True,
        required=False)

    device = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(),
        many=True,
        write_only=True,
        allow_null=True,
        required=False)

    surrounding_facility = CreateSurroundingFacilitySerializer(
        many=True,
        write_only=True,
        allow_null=True,
        required=False)

    class Meta:
        model = Apartment
        exclude = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        facility_data = validated_data.pop('surrounding_facility')

        apartment = super().create(validated_data)

        for facility in facility_data:
            SurroundingFacility.objects.create(apartment=apartment, **facility)

        return apartment
