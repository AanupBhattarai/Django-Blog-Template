# Generated by Django 4.0.1 on 2022-01-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_views_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
