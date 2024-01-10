# booking/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView

from .models import Customer, Service, Booking, MotorcycleBrand, MotorcycleModel
from .forms import CustomerForm, ServiceForm, BookingForm, MotorcycleModelForm

class HomePageView(TemplateView):
    template_name = 'home.html'
class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'customer_list.html', {'customers': customers})

class CustomerCreateView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'customer_form.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'customer_form.html', {'form': form})

class CustomerUpdateView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(instance=customer)
        return render(request, 'customer_form.html', {'form': form, 'customer': customer})

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'customer_form.html', {'form': form, 'customer': customer})

class CustomerDeleteView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, 'customer_confirm_delete.html', {'customer': customer})

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return redirect('customer_list')

class ServiceListView(View):
    def get(self, request):
        services = Service.objects.all()
        return render(request, 'service_list.html', {'services': services})

class ServiceCreateView(View):
    def get(self, request):
        form = ServiceForm()
        return render(request, 'service_form.html', {'form': form})

    def post(self, request):
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
        return render(request, 'service_form.html', {'form': form})

class ServiceUpdateView(View):
    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        form = ServiceForm(instance=service)
        return render(request, 'service_form.html', {'form': form, 'service': service})

    def post(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
        return render(request, 'service_form.html', {'form': form, 'service': service})

class ServiceDeleteView(View):
    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        return render(request, 'service_confirm_delete.html', {'service': service})

    def post(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        service.delete()
        return redirect('service_list')
# Create views for ServiceCreateView, ServiceUpdateView, and ServiceDeleteView in a similar manner as Customer views.

class BookingListView(View):
    def get(self, request):
        bookings = Booking.objects.all()
        return render(request, 'booking_list.html', {'bookings': bookings})

class BookingCreateView(View):
    def get(self, request):
        form = BookingForm()
        return render(request, 'booking_form.html', {'form': form})

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
        return render(request, 'booking_form.html', {'form': form})

class BookingUpdateView(View):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        form = BookingForm(instance=booking)
        return render(request, 'booking_form.html', {'form': form, 'booking': booking})

    def post(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
        return render(request, 'booking_form.html', {'form': form, 'booking': booking})

class BookingDeleteView(View):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        return render(request, 'booking_confirm_delete.html', {'booking': booking})

    def post(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()
        return redirect('booking_list')

class MotorcycleBrandListView(View):
    def get(self, request):
        brands = MotorcycleBrand.objects.all()
        return render(request, 'brand_list.html', {'brands': brands})

# Create a view for MotorcycleBrandDetailView for more information about a specific brand.

class MotorcycleModelListView(ListView):
    model = MotorcycleModel
    template_name = 'model_list.html'

    def get_queryset(self):
        # Retrieve models based on the brand_id from the URL
        brand_id = self.kwargs.get('brand_id')
        return MotorcycleModel.objects.filter(brand_id=brand_id)
    
class MotorcycleModelDetailView(View):
    def get(self, request, model_id):
        model = get_object_or_404(MotorcycleModel, pk=model_id)
        return render(request, 'model_detail.html', {'model': model})

class MotorcycleCreateView(View):
    def get(self, request):
        form = MotorcycleModelForm()
        return render(request, 'motorcycle_create.html', {'form': form})

    def post(self, request):
        form = MotorcycleModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_list')  # Assuming you have a URL named 'model_list'
        return render(request, 'motorcycle_create.html', {'form': form})

class MotorcycleDeleteView(View):
    def get(self, request, model_id):
        motorcycle = get_object_or_404(MotorcycleModel, pk=model_id)
        return render(request, 'motorcycle_confirm_delete.html', {'motorcycle': motorcycle})

    def post(self, request, model_id):
        motorcycle = get_object_or_404(MotorcycleModel, pk=model_id)
        motorcycle.delete()
        return redirect('motorcycle_list')
