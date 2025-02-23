from django.contrib import admin
from .models import Cylinder, Booking, Complaint, Payment

@admin.register(Cylinder)
class CylinderAdmin(admin.ModelAdmin):
    list_display = ('cylinder_id', 'status', 'assigned_to')
    list_filter = ('status',)
    search_fields = ('cylinder_id',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cylinder', 'status', 'booking_date')
    list_filter = ('status',)
    search_fields = ('user__username', 'cylinder__cylinder_id')

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'issue_type', 'status', 'created_at')
    list_filter = ('status', 'issue_type')
    search_fields = ('user__username', 'issue_type')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'booking', 'amount', 'status', 'payment_date')
    list_filter = ('status',)
    search_fields = ('user__username', 'booking__id')