# Generated by Django 3.2.12 on 2023-01-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20230117_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttransaction',
            name='bike',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
