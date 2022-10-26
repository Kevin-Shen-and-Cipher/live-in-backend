from rest_framework import serializers

from job.models import Benefit, City, District, Job, JobPosition, WorkingHour


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class DistrictSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = District
        fields = ['name', 'city']


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ['name']


class WorkingHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHour
        fields = ['name']


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = ['name']


class JobSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()
    job_position = JobPositionSerializer()
    working_hour = WorkingHourSerializer()
    benefit_set = BenefitSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        exclude = ['id', 'created_at', 'updated_at']
        depth = 1
