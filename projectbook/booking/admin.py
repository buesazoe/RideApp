# booking/admin.py
from django.contrib import admin
from .models import Customer, Service, Booking, MotorcycleBrand, MotorcycleModel

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'email')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'motorcycle', 'booking_date', 'start_time', 'end_time')

@admin.register(MotorcycleBrand)
class MotorcycleBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MotorcycleModel)
class MotorcycleModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'production_year')
