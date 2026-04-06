import profile

from django.contrib import admin
from django.contrib.auth.models import User
from financedata.models import Financedata

# Register your models here.
admin.site.register(Financedata)
