# Generated by Django 3.2.8 on 2023-12-06 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_dv'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email_optional',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
