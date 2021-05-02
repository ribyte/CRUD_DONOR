# Generated by Django 3.1.7 on 2021-05-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='billmodel',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=9)),
                ('gender', models.CharField(max_length=1)),
                ('watt_used', models.FloatField()),
                ('payment', models.BooleanField()),
            ],
            options={
                'db_table': 'billtable',
            },
        ),
    ]
