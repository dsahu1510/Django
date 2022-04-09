# Generated by Django 4.0.3 on 2022-04-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=10)),
                ('ename', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=50)),
            ],
        ),
    ]
