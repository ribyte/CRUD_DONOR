from django.db import models
from django.contrib.sites.models import Site

class billmodel(models.Model):
    c_id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=150)
    email=models.CharField(max_length=100)
    job=models.CharField(max_length=9)
    gender=models.CharField(max_length=1)
    watt_used=models.FloatField()
    payment = models.BooleanField()
    site = models.ForeignKey(Site, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        db_table= "billtable"
    