from django.contrib import admin
from users.models import CustomUser, Admin, Patient, Doctor

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Patient)
admin.site.register(Doctor)
