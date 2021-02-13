from django.db import models

# Create your models here.

class userinfo(models.Model): #corresponds to customer table
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # reg_no = models.CharField(max_length=100)
    # room_no = models.CharField(max_length=100)
    username = models.CharField(max_length=20, default = "No name")
    email = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()

class location(models.Model):
    location_id = models.CharField(max_length = 40, primary_key = True)
    name = models.CharField(max_length=40)


class contact_us(models.Model):
    name = models.CharField(max_length=40)
    email =models.CharField(max_length=75)
    subject=models.TextField()
    feed=models.TextField()


class cycle_accessories(models.Model):
    name = models.CharField(max_length=40, primary_key = True)
    quantity = models.IntegerField()
    costperitem = models.IntegerField()

class cycle_category(models.Model):
    name = models.CharField(max_length = 40, primary_key = True)
    costperday = models.IntegerField()
    latefeesperhour = models.IntegerField()

class cycle(models.Model):
    cycle_id = models.CharField(max_length=40, primary_key = True)
    model_year = models.CharField(max_length=5)
    model = models.CharField(max_length=40)
    category = models.ForeignKey(cycle_category, on_delete=models.CASCADE)
    availability = models.CharField(max_length=40)

class discount(models.Model):
    discount_code = models.CharField(max_length = 40, primary_key = True)
    name = models.CharField(max_length=40)
    expiry_date = models.DateField()
    percentage = models.IntegerField()

class insurance(models.Model):
    insurance_code = models.CharField(max_length = 40, primary_key = True)
    name = models.CharField(max_length=40)
    costperday = models.IntegerField()
    coverage_type = models.CharField(max_length = 40)

class Bookings(models.Model):
    user = models.CharField(max_length=40)
    date = models.DateField(max_length=10)
    startpt = models.CharField(max_length=40)
    lastpt = models.CharField(max_length=40)
    start_time = models.TimeField(max_length=40)
    end_time = models.TimeField(max_length=40, default = '24 hours')
    accessory = models.CharField(max_length=40, null = True)
    discount = models.CharField(max_length=40, null = True)
    insurance = models.CharField(max_length=40, null = True)
    cycle_id = models.CharField(max_length=40)
    tot = models.IntegerField()



