# Generated by Django 2.2.5 on 2021-05-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20210428_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='des',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]