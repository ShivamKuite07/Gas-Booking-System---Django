import os
import django
from django.utils import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gasBooking.settings')
django.setup()

from core.models import User, Cylinder, Booking

def book_cylinders():
    # Get users
    raj = User.objects.get(username='raj')
    rohan = User.objects.get(username='rohan')

    # Get available filled cylinders
    filled_cylinders = Cylinder.objects.filter(status='Filled')

    # Raj books a cylinder
    if filled_cylinders.exists():
        raj_cylinder = filled_cylinders.first()
        Booking.objects.create(
            user=raj,
            cylinder=raj_cylinder,
            status='Completed',
            booking_date=timezone.now()
        )
        raj_cylinder.status = 'Assigned'
        raj_cylinder.assigned_to = raj
        raj_cylinder.save()
        print("Raj booked a cylinder successfully.")
    else:
        Booking.objects.create(
            user=raj,
            cylinder=None,
            status='Pending',
            booking_date=timezone.now()
        )
        print("Raj's booking is pending. No filled cylinders available.")

    # Rohan books a cylinder
    if filled_cylinders.exists():
        rohan_cylinder = filled_cylinders.first()
        Booking.objects.create(
            user=rohan,
            cylinder=rohan_cylinder,
            status='Completed',
            booking_date=timezone.now()
        )
        rohan_cylinder.status = 'Assigned'
        rohan_cylinder.assigned_to = rohan
        rohan_cylinder.save()
        print("Rohan booked a cylinder successfully.")
    else:
        Booking.objects.create(
            user=rohan,
            cylinder=None,
            status='Pending',
            booking_date=timezone.now()
        )
        print("Rohan's booking is pending. No filled cylinders available.")

if __name__ == '__main__':
    book_cylinders()