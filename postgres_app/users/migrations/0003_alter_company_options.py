# Generated by Django 4.0.3 on 2022-04-18 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_belongs_to_company_region'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
    ]