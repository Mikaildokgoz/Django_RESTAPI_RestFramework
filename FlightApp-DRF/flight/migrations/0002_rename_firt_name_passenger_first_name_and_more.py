# Generated by Django 4.0.5 on 2022-06-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='firt_name',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='flight',
            name='operation_airlines',
            field=models.CharField(max_length=15),
        ),
    ]
