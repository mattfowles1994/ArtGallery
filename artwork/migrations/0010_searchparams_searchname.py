# Generated by Django 3.1.7 on 2021-03-29 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0009_auto_20210329_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchparams',
            name='searchName',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]