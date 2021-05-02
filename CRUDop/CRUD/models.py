from django.db import models
from django.contrib.sites.models import Site

class billmodel(models.Model):
    donor_id=models.IntegerField(primary_key=True)
    donor_name=models.CharField(max_length=150)
    email=models.CharField(max_length=100)
    blood_group=models.CharField(max_length=9)
    gender=models.CharField(max_length=1)
    donated_amount=models.FloatField()
    prev_donated = models.BooleanField()
    class Meta:
        db_table= "donortable"
    