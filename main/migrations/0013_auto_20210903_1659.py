# Generated by Django 3.2.6 on 2021-09-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210827_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='sap_number',
            field=models.CharField(default='', max_length=8, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='staff_number',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]
