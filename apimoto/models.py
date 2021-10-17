from django.db import models

# Create your models here.

class DataBikes(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    body_type = models.CharField(max_length=100, blank=True, null=True)
    fuel_type = models.CharField(max_length=100, blank=True, null=True)
    engine_description = models.CharField(max_length=255, blank=True, null=True)
    fuel_system = models.CharField(max_length=300, blank=True, null=True)
    cooling = models.CharField(max_length=100, blank=True, null=True)
    displacement = models.CharField(max_length=100, blank=True, null=True)
    max_power = models.CharField(max_length=100, blank=True, null=True)
    max_torque = models.CharField(max_length=100, blank=True, null=True)
    seat_height = models.CharField(max_length=100, blank=True, null=True)
    wet_weight = models.CharField(max_length=100, blank=True, null=True)
    fuel_tank = models.CharField(max_length=100, blank=True, null=True)
    bore = models.CharField(max_length=50, blank=True, null=True)
    stroke = models.CharField(max_length=50, blank=True, null=True)
    clutch = models.CharField(max_length=255, blank=True, null=True)
    front_brake = models.CharField(max_length=500, blank=True, null=True)
    rear_brake = models.CharField(max_length=500, blank=True, null=True)
    front_suspension = models.CharField(max_length=500, blank=True, null=True)
    rear_suspension = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_bikes'

