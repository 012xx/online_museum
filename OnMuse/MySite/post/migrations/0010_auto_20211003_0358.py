# Generated by Django 3.2.7 on 2021-10-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_alter_tag_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200, verbose_name='コメント')),
                ('postid', models.UUIDField(verbose_name='作品ID')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.BigIntegerField(default='1', verbose_name='作者'),
        ),
    ]
