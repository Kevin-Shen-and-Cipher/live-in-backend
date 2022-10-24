from rest_framework import serializers
from .models import City, District, Job, JobPosition, WorkingHour


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = District
        fields = '__all__'


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'


class WorkingHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHour
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()
    job_position = JobPositionSerializer()
    working_hour = WorkingHourSerializer()

    class Meta:
        model = Job
        fields = '__all__'
