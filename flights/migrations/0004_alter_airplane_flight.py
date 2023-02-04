# Generated by Django 4.1.6 on 2023-02-04 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_airplane_flight_airplane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplane',
            name='flight',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='plane', serialize=False, to='flights.flight'),
        ),
    ]
