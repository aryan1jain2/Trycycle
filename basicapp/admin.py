from django.contrib import admin

# Register your models here.
from .models import discount, insurance, userinfo, location, cycle, cycle_accessories, cycle_category, Bookings 

admin.site.register(discount)
admin.site.register(insurance)
admin.site.register(userinfo)
admin.site.register(location)
admin.site.register(cycle)
admin.site.register(cycle_accessories)
admin.site.register(cycle_category)
admin.site.register(Bookings)