# Generated by Django 3.2.6 on 2021-08-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_date_recieved_product_date_received'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.CharField(default=' ', max_length=256),
        ),
    ]
