from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from core.models import Cylinder, Booking, Complaint, Payment
from .forms import BookingForm, ComplaintForm
from django.urls import reverse_lazy
from django.contrib import messages


# User Dashboard View
class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'user_panel/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Get the user's currently owned cylinder
        current_cylinder = Cylinder.objects.filter(assigned_to=user, status='Assigned').first()

        context['current_cylinder'] = current_cylinder
        context['bookings'] = Booking.objects.filter(user=user)
        context['complaints'] = Complaint.objects.filter(user=user)
        context['payments'] = Payment.objects.filter(user=user)
        return context




# Mock payment function
def call_razorpay():
    # Simulate a successful payment
    return True


class BookCylinderView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'user_panel/book_cylinder.html'
    success_url = reverse_lazy('user_dashboard')

    def form_valid(self, form):
        # Call the mock payment function
        payment_successful = call_razorpay()
        if not payment_successful:
            messages.error(self.request, "Payment failed. Please try again.")
            return redirect('book_cylinder')

        # Assign the booking to the logged-in user
        form.instance.user = self.request.user

        # Check if the user already has a cylinder
        current_cylinder = Cylinder.objects.filter(assigned_to=self.request.user, status='Assigned').first()
        if current_cylinder:
            # Mark the current cylinder as empty
            current_cylinder.status = 'Empty'
            current_cylinder.assigned_to = None
            current_cylinder.save()

        # Check for available filled cylinders
        filled_cylinder = Cylinder.objects.filter(status='Filled').first()
        if filled_cylinder:
            # Assign the cylinder and mark booking as completed
            form.instance.cylinder = filled_cylinder
            form.instance.status = 'Completed'
            filled_cylinder.status = 'Assigned'
            filled_cylinder.assigned_to = self.request.user
            filled_cylinder.save()
        else:
            # No filled cylinders available, mark booking as pending
            form.instance.status = 'Pending'

        # Save the booking
        form.save()
        # messages.success(self.request, "Cylinder booked successfully!")
        return super().form_valid(form)



        

# Submit Complaint View
class SubmitComplaintView(LoginRequiredMixin, CreateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'user_panel/submit_complaint.html'
    success_url = reverse_lazy('user_dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# View Booking History
class BookingHistoryView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'user_panel/booking_history.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

# View Complaint Status
class ComplaintStatusView(LoginRequiredMixin, ListView):
    model = Complaint
    template_name = 'user_panel/complaint_status.html'
    context_object_name = 'complaints'

    def get_queryset(self):
        return Complaint.objects.filter(user=self.request.user)