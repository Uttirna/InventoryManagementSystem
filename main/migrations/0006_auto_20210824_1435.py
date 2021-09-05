# Generated by Django 3.2.6 on 2021-08-24 14:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_deletedproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='deletedProductLogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(default=' ', max_length=50)),
                ('serial_num', models.CharField(default=' ', max_length=100, unique=True)),
                ('specification', models.TextField(default=' ')),
                ('date_received', models.DateField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='repairProductLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(default=' ', max_length=50)),
                ('serial_num', models.CharField(default=' ', max_length=100, unique=True)),
                ('specification', models.TextField(default=' ')),
                ('date_received', models.DateField(default=datetime.date.today)),
                ('supplier', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.supplier')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='assign',
            name='id',
        ),
        migrations.RemoveField(
            model_name='repair',
            name='id',
        ),
        migrations.AddField(
            model_name='assign',
            name='date_received',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='assign',
            name='prod_name',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='assign',
            name='serial_num',
            field=models.CharField(default=' ', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='assign',
            name='specification',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='assign',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.supplier'),
        ),
        migrations.AddField(
            model_name='repair',
            name='date_received',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='repair',
            name='prod_name',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='repair',
            name='serial_num',
            field=models.CharField(default=' ', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='repair',
            name='specification',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='assign',
            name='prod_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='repair',
            name='prod_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='deletedProduct',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
