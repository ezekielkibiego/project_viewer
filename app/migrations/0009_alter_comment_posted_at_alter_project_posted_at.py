# Generated by Django 4.2.1 on 2023-06-23 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_comment_posted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted_at',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='project',
            name='posted_at',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime),
        ),
    ]