# Generated by Django 3.2.8 on 2024-02-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0008_remove_operation_value_coin'),
    ]

    operations = [
        migrations.CreateModel(
            name='BANK_NAME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
