# Generated by Django 3.2.7 on 2021-09-28 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customuser',
            table='custom_users',
        ),
    ]
