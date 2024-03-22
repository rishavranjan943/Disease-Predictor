# Generated by Django 5.0.1 on 2024-03-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_patient_address_alter_patient_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_pressure',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='height',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]