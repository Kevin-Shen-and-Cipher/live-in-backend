from django.db import models


class City(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=3, unique=True)


class District(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=5, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class JobPosition(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=30, unique=True)


class WorkingHour(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=10, unique=True)


class Job(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    working_hour = models.ForeignKey(WorkingHour, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()
    tenure = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=100)
    coordinate = models.CharField(max_length=50)
    scroe = models.SmallIntegerField()
    url = models.URLField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
