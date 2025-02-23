import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gasBooking.settings')
django.setup()

from core.models import User

def create_admin():
    # Check if an admin user already exists
    if User.objects.filter(isAdmin=True).exists():
        print("Admin user already exists.")
        return

    # Create the admin user
    admin_user = User.objects.create_user(
        username='admin',
        email='admin@gmail.com',
        password='123',  # Change this to a secure password
        phone='123455555',
        address='Admin Address',
        isAdmin=True
    )
    admin_user.save()
    print("Admin user created successfully.")

if __name__ == '__main__':
    create_admin()