from django.db import models
from job.models import District


class RentType(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'apartment_rent_types'
        verbose_name = "rent_type"
        verbose_name_plural = "rent_types"


class ApartmentType(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'apartment_apartment_types'
        verbose_name = "apartment_type"
        verbose_name_plural = "apartment_types"


class RoomType(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'apartment_room_types'
        verbose_name = "room_type"
        verbose_name_plural = "room_types"


class Restrict(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'apartment_restricts'
        verbose_name = "restrict"
        verbose_name_plural = "restricts"


class Device(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'apartment_devices'
        verbose_name = "device"
        verbose_name_plural = "devices"


class Apartment(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100, default="")
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    coordinate = models.CharField(max_length=50)
    url = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    rent_type = models.ForeignKey(RentType, on_delete=models.CASCADE)
    apartment_type = models.ForeignKey(ApartmentType, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    restrict = models.ManyToManyField(Restrict, blank=True)
    device = models.ManyToManyField(Device, blank=True)

    class Meta:
        db_table = 'apartment_apartments'
        verbose_name = "apartment"
        verbose_name_plural = "apartments"


class FacilityType(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'apartment_facility_types'
        verbose_name = "facility_type"
        verbose_name_plural = "facility_types"


class SurroundingFacility(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=30)
    facility_type = models.ForeignKey(FacilityType, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'apartment_surrounding_facilities'
        verbose_name = "surrounding_facility"
        verbose_name_plural = "surrounding_facilities"
