# Generated by Django 3.2.8 on 2024-02-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0096_auto_20240221_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='I3YIKdUjAK', max_length=10),
        ),
    ]
