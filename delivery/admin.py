from django.contrib import admin
from .models import Address, Restaurant, Menu, MenuItem, Order, OrderItem, Delivery

admin.site.register(Address)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Delivery)
