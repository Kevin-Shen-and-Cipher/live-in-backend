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


class ListJobSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)

    job_position = JobPositionSerializer(read_only=True)

    working_hour = WorkingHourSerializer(read_only=True)

    benefit = BenefitSerializer(
        source='benefit_set',
        many=True,
        read_only=True)

    class Meta:
        model = Job
        exclude = ['id', 'created_at', 'updated_at']


class CreateJobSerializer(serializers.ModelSerializer):
    district = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all(),
        write_only=True)

    job_position = serializers.PrimaryKeyRelatedField(
        queryset=JobPosition.objects.all(),
        write_only=True)

    working_hour = serializers.PrimaryKeyRelatedField(
        queryset=WorkingHour.objects.all(),
        write_only=True)

    benefit = BenefitSerializer(
        many=True,
        write_only=True,
        allow_null=True,
        required=False)

    class Meta:
        model = Job
        exclude = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        benefit_data = validated_data.pop('benefit')

        job = super().create(validated_data)

        for benefit in benefit_data:
            Benefit.objects.create(job=job, **benefit)

        return job
