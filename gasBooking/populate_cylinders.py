import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gasBooking.settings')
django.setup()

from core.models import Cylinder

def populate_cylinders():
    # Create 6 filled cylinders
    import random
    import string

    for i in range(6):
        cylinder_id = ''.join(random.choices(string.ascii_uppercase, k=3) + random.choices(string.digits, k=3))
        Cylinder.objects.create(
            cylinder_id=cylinder_id,  # e.g., ABC123, XYZ789, etc.
            status='Filled'
        )
    print("Created 6 filled cylinders.")

    # Create 4 empty cylinders
    for i in range(4):
        cylinder_id = ''.join(random.choices(string.ascii_uppercase, k=3) + random.choices(string.digits, k=3))
        Cylinder.objects.create(
            cylinder_id=cylinder_id,  # e.g., ABC123, XYZ789, etc.
            status='Empty'
        )
    print("Created 4 empty cylinders.")

    print("Cylinders populated successfully.")

if __name__ == '__main__':
    populate_cylinders()