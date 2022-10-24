from django.db import models
from job.models import District


class RentType(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=10, unique=True)


class ApartmentType(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=10, unique=True)


class RoomType(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=10, unique=True)


class Restrict(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=20, unique=True)


class Device(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=10, unique=True)


class Apartment(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    rent_type = models.ForeignKey(RentType, on_delete=models.CASCADE)
    apartment_type = models.ForeignKey(ApartmentType, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    restrict = models.ManyToManyField(Restrict)
    device = models.ManyToManyField(Device)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    coordinate = models.CharField(max_length=50)
    scroe = models.SmallIntegerField()
    url = models.URLField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
