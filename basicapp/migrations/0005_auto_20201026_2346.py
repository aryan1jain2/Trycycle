# Generated by Django 3.1.2 on 2020-10-26 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0004_auto_20201026_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='accessory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basicapp.cycle_accessories'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basicapp.discount'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='insurance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basicapp.insurance'),
        ),
    ]
