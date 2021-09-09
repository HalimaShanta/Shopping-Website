from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Home)
admin.site.register(Beauty)
admin.site.register(Access)
admin.site.register(Store)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','rate','created_at','avg']
    readonly_fields = ['created_at']
