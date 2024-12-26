# Generated by Django 5.1.4 on 2024-12-26 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=50)),
                ('admin_email', models.EmailField(max_length=50, unique=True)),
                ('admin_phone_no', models.IntegerField(max_length=10, unique=True)),
                ('admin_address', models.CharField(max_length=50)),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('farmer_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('farmer_name', models.CharField(max_length=50)),
                ('farmer_email', models.EmailField(max_length=50, unique=True)),
                ('farmer_phone_no', models.IntegerField(max_length=10, unique=True)),
                ('farmer_address', models.CharField(max_length=50)),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('gateway_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('mac_id', models.IntegerField(max_length=10)),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('motor_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('mac_id', models.IntegerField(max_length=10)),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('sensor_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('mac_id', models.IntegerField(max_length=10)),
                ('sensor_type', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Valve',
            fields=[
                ('valve_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('mac_id', models.IntegerField(max_length=10)),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gateway_Farmer',
            fields=[
                ('gateway_farmer_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
                ('farmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_app.farmer')),
                ('gateway_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_app.gateway')),
            ],
        ),
        migrations.CreateModel(
            name='Motor_Farmer',
            fields=[
                ('motor_farmer_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
                ('farmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_app.farmer')),
                ('motor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_app.motor')),
            ],
        ),
        migrations.CreateModel(
            name='Motor_Operation',
            fields=[
                ('motor_operation_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('motor_status', models.CharField(max_length=50)),
                ('current_timestamp', models.DateTimeField()),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
                ('motor_farmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_app.motor_farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor_Farmer',
            fields=[
                ('sensor_farmer_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
                ('farmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_app.farmer')),
                ('sensor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_app.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor_Data',
            fields=[
                ('sensor_data_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('sensor_data_value', models.CharField(max_length=50)),
                ('current_timestamp', models.DateTimeField()),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
                ('sensor_farmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_app.sensor_farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Valve_Farmer',
            fields=[
                ('valve_farmer_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
                ('farmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_app.farmer')),
                ('valve_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_app.valve')),
            ],
        ),
        migrations.CreateModel(
            name='Valve_Operation',
            fields=[
                ('valve_operation_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('valve_status', models.CharField(max_length=50)),
                ('current_timestamp', models.DateTimeField()),
                ('extra_field1', models.CharField(max_length=50)),
                ('extra_field2', models.CharField(max_length=50)),
                ('extra_field3', models.CharField(max_length=50)),
                ('valve_farmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agri_app.valve_farmer')),
            ],
        ),
    ]
