# Generated by Django 3.1.7 on 2021-03-07 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0004_auto_20210307_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='images',
            field=models.ImageField(default='AG\\static\x07pp\\images\\default.PNG', upload_to=''),
        ),
    ]
