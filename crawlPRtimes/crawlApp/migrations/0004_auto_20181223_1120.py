# Generated by Django 2.0.9 on 2018-12-23 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawlApp', '0003_auto_20181223_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
    ]
