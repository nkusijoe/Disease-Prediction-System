# Generated by Django 4.2.3 on 2023-07-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200118_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='State_Medical_Council',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='qualification',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='registration_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=50),
        ),
    ]
