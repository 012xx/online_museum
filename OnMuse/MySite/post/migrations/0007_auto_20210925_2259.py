# Generated by Django 3.2.7 on 2021-09-25 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20210925_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
