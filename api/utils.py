from django.contrib.auth import authenticate
from django.utils import timezone
from django.db.models import Q,F
from rest_framework import serializers
import datetime
from .models import *


def get_and_authenticate_user(username, password):
    user = authenticate(username=username, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password")
    return user

def create_user_account(username,password,first_name,last_name,email,phone,location_gu,location_dong,**extra_fields):
    user =User.objects.create_user(username=username,password=password,
                                  first_name=first_name,last_name=last_name,
                                  email=email,phone=phone,
                                  location_gu=location_gu,location_dong=location_dong,
                                  **extra_fields)
    return user

def expire_enrollments():
    enrollments=Enrollment.objects.filter(Q(end_date__lt=timezone.now().date())|Q(left_count__lte=0))
    enrollments.update(valid=False)
    expired_enrollment_ids=enrollments.values_list('id',flat=True)
    CourseTime.objects.filter(enrollment_id__in=expired_enrollment_ids).update(taken=False,enrollment_id=None)

def update_enrollment_left_count(user):
    user.enrollments.all().filter(valid=True,
                                  lesson_day=datetime.datetime.today().weekday(),
                                  lesson_time__lte=datetime.datetime.now().hour).update(left_count=F('left_count') - 1)
    expire_enrollments()


