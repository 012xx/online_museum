# Generated by Django 3.2.9 on 2021-12-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_alter_exhibition_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_exhibition',
            field=models.BooleanField(default=False, help_text='exhibitionだったらTrue'),
        ),
    ]
