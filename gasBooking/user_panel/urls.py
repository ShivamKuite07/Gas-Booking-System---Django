from django.urls import path
from .views import (
    UserDashboardView,
    BookCylinderView,
    SubmitComplaintView,
    BookingHistoryView,
    ComplaintStatusView,
)

urlpatterns = [
    path('dashboard/', UserDashboardView.as_view(), name='user_dashboard'),
    path('book-cylinder/', BookCylinderView.as_view(), name='book_cylinder'),
    path('submit-complaint/', SubmitComplaintView.as_view(), name='submit_complaint'),
    path('booking-history/', BookingHistoryView.as_view(), name='booking_history'),
    path('complaint-status/', ComplaintStatusView.as_view(), name='complaint_status'),
]