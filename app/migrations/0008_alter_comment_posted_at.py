# Generated by Django 4.2.1 on 2023-06-23 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_comment_posted_at_alter_like_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted_at',
            field=models.DateTimeField(verbose_name=datetime.datetime),
        ),
    ]
