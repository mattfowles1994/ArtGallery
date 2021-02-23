# Generated by Django 2.0.7 on 2021-01-31 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('width', models.TextField()),
                ('height', models.TextField()),
                ('artist', models.TextField(default='V.Galvao')),
                ('available', models.TextField(default='No')),
            ],
        ),
    ]
