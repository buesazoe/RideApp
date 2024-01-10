# booking/forms.py
from django import forms
from .models import Customer, Service, Booking, MotorcycleModel

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'phone_number', 'email']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'motorcycle', 'booking_date', 'start_time', 'end_time']

class MotorcycleModelForm(forms.ModelForm):
    class Meta:
        model = MotorcycleModel
        fields = '__all__'
