from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, TemplateView
from core.models import Cylinder, Booking, Complaint, Payment
from django.urls import reverse_lazy


# Admin Dashboard View
class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admin_panel/dashboard.html'

    def test_func(self):
        return self.request.user.isAdmin

# Manage Cylinders
class CylinderListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Cylinder
    template_name = 'admin_panel/cylinder_list.html'
    context_object_name = 'cylinders'

    def test_func(self):
        return self.request.user.isAdmin

class CylinderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cylinder
    fields = ['status', 'assigned_to']
    template_name = 'admin_panel/cylinder_update.html'
    success_url = reverse_lazy('admin_cylinder_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Add CSS classes to form fields
        form.fields['status'].widget.attrs.update({'class': 'form-control'})
        form.fields['assigned_to'].widget.attrs.update({'class': 'form-control'})
        return form
    

    def test_func(self):
        return self.request.user.isAdmin

# Manage Bookings
class BookingListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Booking
    template_name = 'admin_panel/booking_list.html'
    context_object_name = 'bookings'

    def test_func(self):
        return self.request.user.isAdmin

class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    fields = ['status']
    template_name = 'admin_panel/booking_update.html'
    success_url = reverse_lazy('admin_booking_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Add CSS classes to form fields
        form.fields['status'].widget.attrs.update({'class': 'form-control'})
        return form

    def test_func(self):
        return self.request.user.isAdmin

# Manage Complaints

class ComplaintListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Complaint
    template_name = 'admin_panel/complaint_list.html'
    context_object_name = 'complaints'

    def test_func(self):
        return self.request.user.isAdmin

class ComplaintUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Complaint
    fields = ['status']
    template_name = 'admin_panel/complaint_update.html'
    success_url = reverse_lazy('admin_complaint_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Add CSS classes to form fields
        form.fields['status'].widget.attrs.update({'class': 'form-control'})
        return form

    def test_func(self):
        return self.request.user.isAdmin

# Manage Payments
class PaymentListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Payment
    template_name = 'admin_panel/payment_list.html'
    context_object_name = 'payments'

    def test_func(self):
        return self.request.user.isAdmin