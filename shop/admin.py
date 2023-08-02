from django.contrib import admin

# Register your models here.

from .models import product, contact, order, orderUpdate

admin.site.register(product)
admin.site.register(contact)
admin.site.register(order)
admin.site.register(orderUpdate)