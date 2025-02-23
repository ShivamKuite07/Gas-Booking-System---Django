import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gasBooking.settings')
django.setup()

from core.models import User

def add_users():
    # Create user 'raj'
    raj = User.objects.create_user(
        username='raj',
        email='raj@gmail.com',
        password='123',  
        phone='1234567890',
        address='Raj Address',
        isAdmin=False  # Normal user
    )
    raj.save()
    print("User 'raj' created successfully.")

    # Create user 'rohan'
    rohan = User.objects.create_user(
        username='rohan',
        email='rohan@gmail.com',
        password='123',  
        phone='0987654321',
        address='Rohan Address',
        isAdmin=False  # Normal user
    )
    rohan.save()
    print("User 'rohan' created successfully.")

if __name__ == '__main__':
    add_users()