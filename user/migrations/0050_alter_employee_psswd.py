# Generated by Django 3.2.8 on 2023-12-28 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0049_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='SFD8DowssWOLgPzhSjwK', max_length=20, unique=True),
        ),
    ]
