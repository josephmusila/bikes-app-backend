# Generated by Django 4.1.3 on 2022-12-03 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_customer_repairservices_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairservices',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
