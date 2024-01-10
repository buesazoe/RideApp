# booking/models.py
from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MotorcycleBrand(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class MotorcycleModel(BaseModel):
    brand = models.ForeignKey(MotorcycleBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    production_year = models.IntegerField()

    def __str__(self):
        return f'{self.brand} - {self.name} ({self.production_year})'

class Customer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

class Booking(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    motorcycle = models.ForeignKey(MotorcycleModel, on_delete=models.CASCADE)
    booking_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.customer} - {self.motorcycle} ({self.booking_date})'

class Service(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - ${self.price}'
