from django.contrib import admin
from .models import walletData, DataUser

# Register your models here.
admin.site.register(DataUser)
admin.site.register(walletData)