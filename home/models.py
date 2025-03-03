# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    customer  = models.CharField(max_length=255, null=True, blank=True)
    employee = models.CharField(max_length=255, null=True, blank=True)
    admin = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Vin(models.Model):

    #__Vin_FIELDS__
    vin_number = models.CharField(max_length=255, null=True, blank=True)

    #__Vin_FIELDS__END

    class Meta:
        verbose_name        = _("Vin")
        verbose_name_plural = _("Vin")


class Vehiclestatus(models.Model):

    #__Vehiclestatus_FIELDS__
    vin_number = models.ForeignKey(Vin, on_delete=models.CASCADE)
    accident_history = models.CharField(max_length=255, null=True, blank=True)
    odometer_fraud = models.CharField(max_length=255, null=True, blank=True)
    theft_involvement = models.CharField(max_length=255, null=True, blank=True)

    #__Vehiclestatus_FIELDS__END

    class Meta:
        verbose_name        = _("Vehiclestatus")
        verbose_name_plural = _("Vehiclestatus")


class Specs(models.Model):

    #__Specs_FIELDS__
    vin_number = models.ForeignKey(Vin, on_delete=models.CASCADE)
    make = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    body_type = models.CharField(max_length=255, null=True, blank=True)
    interior_color = models.CharField(max_length=255, null=True, blank=True)
    exterior_color = models.CharField(max_length=255, null=True, blank=True)
    manufacture_year = models.CharField(max_length=255, null=True, blank=True)
    engine_code = models.CharField(max_length=255, null=True, blank=True)
    powertrain_power = models.CharField(max_length=255, null=True, blank=True)

    #__Specs_FIELDS__END

    class Meta:
        verbose_name        = _("Specs")
        verbose_name_plural = _("Specs")


class Inspection(models.Model):

    #__Inspection_FIELDS__
    year = models.CharField(max_length=255, null=True, blank=True)
    inpection_result = models.CharField(max_length=255, null=True, blank=True)
    rating = models.CharField(max_length=255, null=True, blank=True)
    inspection_date = models.CharField(max_length=255, null=True, blank=True)
    link_to_results = models.CharField(max_length=255, null=True, blank=True)

    #__Inspection_FIELDS__END

    class Meta:
        verbose_name        = _("Inspection")
        verbose_name_plural = _("Inspection")


class History(models.Model):

    #__History_FIELDS__
    mileage_at_service = models.CharField(max_length=255, null=True, blank=True)
    worked_perfomed = models.CharField(max_length=255, null=True, blank=True)
    perfomed_by = models.CharField(max_length=255, null=True, blank=True)
    cost = models.CharField(max_length=255, null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)

    #__History_FIELDS__END

    class Meta:
        verbose_name        = _("History")
        verbose_name_plural = _("History")



#__MODELS__END
