# Generated by Django 5.0.1 on 2024-03-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_patient_address_alter_patient_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
