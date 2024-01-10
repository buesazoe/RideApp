"""
URL configuration for projectbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from booking.views import (
    HomePageView,
    CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,
    ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView,
    BookingListView, BookingCreateView, BookingUpdateView, BookingDeleteView,
    MotorcycleBrandListView, MotorcycleModelListView, MotorcycleModelDetailView,MotorcycleCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),

    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    path('services/', ServiceListView.as_view(), name='service_list'),
    path('services/create/', ServiceCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/update/', ServiceUpdateView.as_view(), name='service_update'),
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),

    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('bookings/create/', BookingCreateView.as_view(), name='booking_create'),
    path('bookings/<int:pk>/update/', BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),

    path('brands/', MotorcycleBrandListView.as_view(), name='brand_list'),
    
    path('models/', MotorcycleModelListView.as_view(), name='model_list'),
    path('models/<int:model_id>/', MotorcycleModelDetailView.as_view(), name='model_detail'),
    path('models/create/', MotorcycleCreateView.as_view(), name='motorcycle_create'),
]
