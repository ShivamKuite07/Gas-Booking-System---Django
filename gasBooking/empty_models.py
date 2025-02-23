import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gasBooking.settings')
django.setup()

from core.models import Cylinder, Booking, Complaint, Payment, User

def empty_models():


    # Delete all users excepts admin
    # User.objects.exclude(username='admin').delete()
    # print("Deleted all users except admin.")

    # Delete all users
    User.objects.all().delete()
    print("Deleted all users.")

    # Delete all cylinders
    Cylinder.objects.all().delete()
    print("Deleted all cylinders.")

    # Delete all bookings
    Booking.objects.all().delete()
    print("Deleted all bookings.")

    # Delete all complaints
    Complaint.objects.all().delete()
    print("Deleted all complaints.")

    # Delete all payments
    Payment.objects.all().delete()
    print("Deleted all payments.")

    print("All models have been emptied.")

if __name__ == '__main__':
    empty_models()