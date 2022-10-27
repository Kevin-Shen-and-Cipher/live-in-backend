from django.db import models


class City(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=3, unique=True)

    class Meta:
        db_table = 'cities'
        verbose_name = "city"
        verbose_name_plural = "cities"


class District(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=5, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = 'districts'
        verbose_name = "district"
        verbose_name_plural = "districts"


class JobPosition(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'job_job_positions'
        verbose_name = "job_position"
        verbose_name_plural = "job_positions"


class WorkingHour(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'job_working_hours'
        verbose_name = "working_hour"
        verbose_name_plural = "working_hours"


class Job(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100, default="")
    salary = models.PositiveIntegerField()
    tenure = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=100)
    coordinate = models.CharField(max_length=50)
    url = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    working_hour = models.ForeignKey(WorkingHour, on_delete=models.CASCADE)

    class Meta:
        db_table = 'job_jobs'
        verbose_name = "job"
        verbose_name_plural = "jobs"


class Benefit(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=30)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    class Meta:
        db_table = 'job_benefits'
        verbose_name = "benefit"
        verbose_name_plural = "benefits"
