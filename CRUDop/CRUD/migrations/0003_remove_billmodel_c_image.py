# Generated by Django 3.1.7 on 2021-05-02 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0002_auto_20210502_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billmodel',
            name='c_image',
        ),
    ]