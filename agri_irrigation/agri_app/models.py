from django.db import models
from django.contrib.auth.models import User
import uuid

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"

# Create your models here.
class Agri_admin(models.Model):
    admin_id = models.AutoField(primary_key=True, null=False)
    admin_name = models.CharField(max_length=50, null=False)
    admin_email = models.EmailField(max_length=50, null=False, unique=True)
    admin_phone_no = models.IntegerField(null=False, unique=True)
    admin_address = models.CharField(max_length=50, null=False)
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)

class Farmer(models.Model):
    farmer_id = models.AutoField(primary_key=True, null=False)
    farmer_name = models.CharField(max_length=50, null=False)
    farmer_email = models.EmailField(max_length=50, null=False, unique=True)
    farmer_phone_no = models.IntegerField(null=False, unique=True)
    farmer_address = models.CharField(max_length=50, null=False)
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)

class Gateway(models.Model):
    gateway_id = models.AutoField(primary_key=True, null=False)
    mac_id = models.IntegerField(null=False)
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)


class Gateway_Farmer(models.Model):
    gateway_farmer_id = models.AutoField(primary_key=True, null=False)
    gateway_id = models.ForeignKey(Gateway, on_delete=models.CASCADE, null=False)
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=False)
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)

class Sensor(models.Model):
    sensor_id = models.AutoField(primary_key=True, null=False)
    mac_id = models.IntegerField(null=False)
    sensor_type = models.CharField(max_length=50, null=False)
    unit = models.CharField(max_length=50, null=False)
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)

class Sensor_Farmer(models.Model):
    sensor_farmer_id = models.AutoField(primary_key=True, null=False)
    sensor_id  = models.ForeignKey(Sensor, on_delete=models.CASCADE, null=False)
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=False)
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)

class Sensor_Data(models.Model):
    sensor_data_id = models.AutoField(primary_key=True, null=False)
    sensor_farmer_id = models.ForeignKey(Sensor_Farmer, on_delete=models.CASCADE, null=False)
    sensor_data_value = models.CharField(max_length=50, null=False)
    current_timestamp = models.DateTimeField()
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)

class Motor(models.Model):
    motor_id = models.AutoField(primary_key=True, null=False)
    mac_id = models.IntegerField(null=False)
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)

class Motor_Farmer(models.Model):
    motor_farmer_id = models.AutoField(primary_key=True, null=False)
    motor_id = models.ForeignKey(Motor, on_delete=models.CASCADE, null=False)
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=False)
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)

class Motor_Operation(models.Model):
    motor_operation_id = models.AutoField(primary_key=True, null=False)
    motor_farmer_id = models.ForeignKey(Motor_Farmer, on_delete=models.CASCADE, null=False)
    motor_status = models.CharField(max_length=50, null=False)
    current_timestamp = models.DateTimeField()
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)

class Valve(models.Model):
    valve_id = models.AutoField(primary_key=True, null=False)
    mac_id = models.IntegerField(null=False)
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)

class Valve_Farmer(models.Model):
    valve_farmer_id = models.AutoField(primary_key=True, null=False)
    valve_id = models.ForeignKey(Valve, on_delete=models.CASCADE, null=False)
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=False)
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)

class Valve_Operation(models.Model):
    valve_operation_id = models.AutoField(primary_key=True, null=False)
    valve_farmer_id = models.ForeignKey(Valve_Farmer, on_delete=models.CASCADE, null=False)
    valve_status = models.CharField(max_length=50, null=False)
    current_timestamp = models.DateTimeField()
    extra_field1 = models.CharField(max_length=50, null=True)
    extra_field2 = models.CharField(max_length=50, null=True)
    extra_field3 = models.CharField(max_length=50, null=True)


