# Generated by Django 3.0.6 on 2022-03-24 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]