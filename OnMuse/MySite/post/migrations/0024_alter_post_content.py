# Generated by Django 3.2.9 on 2021-12-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_post_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=44, verbose_name='本文'),
        ),
    ]
