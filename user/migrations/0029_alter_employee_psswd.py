# Generated by Django 3.2.8 on 2023-10-26 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_auto_20231019_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='S3GQUYaWZKIc7SPFoyVt', max_length=20, unique=True),
        ),
    ]
