# Generated by Django 5.1.4 on 2024-12-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_stock_createdby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
