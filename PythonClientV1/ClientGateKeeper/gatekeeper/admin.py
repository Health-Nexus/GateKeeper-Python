from django.contrib import admin

# Register your models here.
from .models import Details
from .models import Accounts

admin.site.register(Details)
