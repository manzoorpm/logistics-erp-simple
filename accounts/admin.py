from django.contrib import admin
from .models import *

admin.site.register(Warehouse)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)