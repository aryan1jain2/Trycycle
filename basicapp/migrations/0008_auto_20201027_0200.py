# Generated by Django 3.1.2 on 2020-10-26 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0007_bookings_cycle_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='accessory',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='cycle_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='discount',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='insurance',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='lastpt',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='startpt',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='user',
            field=models.CharField(max_length=40),
        ),
    ]
