# Generated by Django 3.2.7 on 2021-11-01 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_auto_20211029_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='postid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]
