# Generated by Django 4.2.11 on 2024-04-22 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='secondary_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
