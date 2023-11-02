from django.db import models

# Create your models here.

class ConnectionElementView(models.Model):
    company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=255)
    country_id = models.IntegerField()
    country_name = models.CharField(max_length=255)
    region_id = models.IntegerField()
    region_name = models.CharField(max_length=255)
    area_id = models.IntegerField()
    area_name = models.CharField(max_length=255)
    area_short_name = models.CharField(max_length=255)
    connection_element_id = models.IntegerField()
    connection_element_name = models.CharField(max_length=255)
    connection_element_type_id = models.IntegerField()
    connection_element_type_name = models.CharField(max_length=255)