# Generated by Django 2.2.4 on 2019-09-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('punjabi', '0003_auto_20190903_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roombook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm', models.CharField(max_length=80)),
                ('uid', models.CharField(max_length=40)),
                ('no', models.CharField(max_length=15)),
                ('adds', models.CharField(max_length=200)),
                ('rid', models.CharField(max_length=50)),
                ('room_name', models.CharField(max_length=80)),
                ('price', models.CharField(max_length=80)),
                ('startdate', models.CharField(max_length=80)),
                ('enddate', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='booking',
        ),
    ]