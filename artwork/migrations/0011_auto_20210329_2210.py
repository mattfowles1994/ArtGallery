# Generated by Django 3.1.7 on 2021-03-29 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0010_searchparams_searchname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SearchParams',
            new_name='SearchParam',
        ),
    ]
