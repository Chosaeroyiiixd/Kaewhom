# Generated by Django 2.2.5 on 2021-04-22 17:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210422_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='joined_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
