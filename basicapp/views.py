from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import userinfo, Bookings, contact_us, discount, cycle, cycle_category, location, insurance, cycle_accessories
from django.http import HttpResponse, HttpResponseRedirect
from collections import deque, namedtuple
from datetime import datetime, date
from django.db import connection
import numpy as np
import math

# Create your views here.
def index(request):
    discount_list = discount.objects.order_by('name')
    # date_dict = {'discount' : discount_list}
    cycle_cat_list = cycle_category.objects.order_by('name')
    location_list = location.objects.order_by('name')
    insurance_list = insurance.objects.order_by('name')
    cycle_acc_list = cycle_accessories.objects.order_by('name')
    context_dict = { 'cycle_category' : cycle_cat_list, 'discount' : discount_list, 'location' : location_list, 'insurance' : insurance_list, 'cycle_accessories' : cycle_acc_list}
    return render(request,'TryCycle.html',context = context_dict)

def register(request):

    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone_no=request.POST['phone_no']
        # reg_no=request.POST['reg_no']
        # room_no=request.POST['room_no']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                # userinfos=userinfo(email=email,first_name=first_name,last_name=last_name,reg_no=reg_no,room_no=room_no,phone_no=phone_no)
                userinfos=userinfo(email=email,first_name=first_name,last_name=last_name,phone_no=phone_no)
                user.save()
                userinfos.save()
                messages.info(request,'user created')
            return redirect('/')
        else:
            messages.info(request,'Password does not match')
            return redirect('/')

    else:
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect("/")
        else:
            messages.error(request,'invalid cedentials')
            return redirect('/')
    else:
        return redirect('/')

def fare(request):
        return render(request,'/fare')


def rent_now(request):
    if request.method == 'POST':
        
        # username = None
        username = request.user.username
        date=request.POST['date']
        start_time=request.POST['st']
        end_time=request.POST['et']
        startpt=request.POST['check']
        lastpt=request.POST['end']
        cat=request.POST['cat']
        accessory_name=request.POST.get('acc',None)
        discount_name=request.POST.get('disc',None) #returns a string containing the discount name. eg. 'CTS CORPORATE'
        insurance_name=request.POST.get('ins',None)
        

        cycle_list = cycle.objects.order_by('cycle_id')
        cycle_id = '1234'

        discount_list = discount.objects.order_by('name')

        insurance_list = insurance.objects.order_by('name')

        accessory_list = cycle_accessories.objects.order_by('name')


        id_list = set()
        for cycles in cycle.objects.filter(availability__exact = 'Not Available'):
            id_list.add(cycles.cycle_id)


        id_list = list(id_list)

        print(id_list)

        final_list = []

        for cycle_id in id_list:
            print(Bookings.objects.filter(cycle_id__exact = cycle_id).order_by('id'), '1234')
            if not Bookings.objects.filter(cycle_id__exact = cycle_id).order_by('id'):
                pass
            else:
                booking = Bookings.objects.filter(cycle_id__exact = cycle_id).order_by('id').last()
                temp = booking.date
                # date = datetime.strptime(temp, '%Y-%m-%d')
                endtime = booking.end_time
                starttime = booking.start_time
                today = datetime.now().date()
                now = datetime.now().time()
                if today >= temp:
                    if now > endtime > starttime:
                        final_list.append(cycle_id)
                    else:
                        print("error")
                else:
                    print("error")

        print(final_list, '12345')
        for cycles in final_list:
            temp = cycle.objects.filter(cycle_id__exact = cycles)[0]
            temp.availability = 'Available'
            temp.save()
            # for a in temp:
            #     a.save()
            


        for cycles in cycle.objects.filter(category__exact = cat, availability__exact = 'Available'): 
            cycle_id = cycles.cycle_id
            cat_cost = cycles.category.costperday
            cycles.availability = 'Not Available'
            cycles.save()
            # print(cat_cost)
            break
        else:
            # redirect('/')
            messages.success(request, 'Please choose another category!')
            return HttpResponseRedirect('/')


        disamt = 0
        if discount_name != None:
            for disc in discount_list:
                if disc.name == discount_name:
                    disamt = disc.percentage
                    break

        print('discount percentage is ', disamt)

        cursor = connection.cursor()
        print(cursor.execute('Select * from basicapp_cycle'))


        insamt = 0
        if insurance_name != None:
            for ins in insurance_list:
                if ins.name == insurance_name:
                    insamt = ins.costperday
                    break

        print('insurance cost per day', insamt)

        accamt = 0
        if( accessory_name != None):
            for acc in accessory_list:
                if acc.name == accessory_name:
                    accamt = acc.costperitem * acc.quantity 
                    break

        print('accessory amount is ', accamt)

        time_elapsed = datetime.strptime(end_time,'%H:%M') - datetime.strptime(start_time,'%H:%M')

        seconds = time_elapsed.seconds
        hours = seconds//3600
        cost = (hours+1)*math.ceil(float(cat_cost/24)) - disamt*0.01*(hours+1)*(cat_cost)/24 + (insamt/24) + accamt
        if cost <= 0:
            cost = 2
        # print(cost)
        booked=Bookings(user=username,date=date,startpt=startpt,lastpt=lastpt,start_time = start_time, end_time = end_time, accessory = accessory_name, discount = discount_name, insurance = insurance_name, cycle_id = cycle_id, tot=cost)
        booked.save()
        # print(cycle_list, type(cycle_list))

        # bill = billing(user = username, bill_date = date, bill_status = 'Confirmed', discount_amount = disamt, total_amount = cost+1, tax_amount = 1, total_late_fee = 0 )
        # bill.save()

        
        # flag = 0

        # while(flag==0):
        #     if (start_time > end_time):
        #         for cycles in cycle_list: 
        #             if (cycles.cycle_id == cycle_id):
        #                 quantity = quantity + 1
        #                 flag = 1
        #                 break 
        return redirect('/')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        feed=request.POST['feed']
        contacted=contact_us(name=name,email=email,subject=subject,feed=feed)

        contacted.save()
        return redirect('/')

def mybookings(request):
    booking_list = Bookings.objects.order_by('id')
    date_dict = {'bookings':booking_list}
    return render(request,'mybookings.html',context=date_dict)

def bicycle(request):
    return render(request,'bicycle.html')

