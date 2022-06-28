from django.contrib import admin
from .models import balance,expences,update_balance
# Register your models here.
admin.site.register(balance)
admin.site.register(expences)
admin.site.register(update_balance)