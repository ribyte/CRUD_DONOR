from django.db import models

class billModel(models.Model):
    c_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=1)
    watt_used=models.FloatField()
    class meta:
        db_table= "billmodel"
    