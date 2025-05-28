from django.contrib import admin
from .models import *


# Register your models here.

# CarModelInline class
class CarModelInLine(admin.StackedInline):
    model = CarModel
    extra = 2

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("car_make", "name", "type", "year", "dealer_id")
    list_filter = ("car_make", "type", "year")
    search_fields = ["name"]
    
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInLine]
    list_display = ("name", "description")


# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)
