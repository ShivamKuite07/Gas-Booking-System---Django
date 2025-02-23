from django.urls import path
from .views import (
    AdminDashboardView,
    CylinderListView, CylinderUpdateView,
    BookingListView, BookingUpdateView,
    ComplaintListView, ComplaintUpdateView,
    PaymentListView,
)

urlpatterns = [
    path('dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('cylinders/', CylinderListView.as_view(), name='admin_cylinder_list'),
    path('cylinders/<int:pk>/update/', CylinderUpdateView.as_view(), name='admin_cylinder_update'),
    path('bookings/', BookingListView.as_view(), name='admin_booking_list'),
    path('bookings/<int:pk>/update/', BookingUpdateView.as_view(), name='admin_booking_update'),
    path('complaints/', ComplaintListView.as_view(), name='admin_complaint_list'),
    path('complaints/<int:pk>/update/', ComplaintUpdateView.as_view(), name='admin_complaint_update'),
    path('payments/', PaymentListView.as_view(), name='admin_payment_list'),
]