# Generated by Django 3.2.8 on 2024-01-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0062_alter_employee_psswd'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='internal_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='npUqrPFogMDEdY3aOyAx', max_length=20, unique=True),
        ),
    ]
