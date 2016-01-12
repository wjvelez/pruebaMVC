from django.contrib import admin

from .models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['orderid', 'customerid']

admin.site.register(Orders, OrdersAdmin)

#user:      root
#email:
#password:  practicamvc
