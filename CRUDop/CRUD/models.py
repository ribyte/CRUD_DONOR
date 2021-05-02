from django.db import models

class billmodel(models.Model):
    c_id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=150)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=1)
    watt_used=models.IntegerField()
    
    class Meta:
        db_table= "billModel"
    