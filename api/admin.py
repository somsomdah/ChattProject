from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(RelatedLocation)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(ClassTime)