import os
import django
from django.utils import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gasBooking.settings')
django.setup()

from core.models import User, Complaint

def make_complaint():
    # Get user 'raj'
    raj = User.objects.get(username='raj')

    # Raj makes a complaint
    Complaint.objects.create(
        user=raj,
        issue_type='Gas Leak',
        description='Gas leak detected in the kitchen.',
        status='Pending',
        created_at=timezone.now()
    )
    print("Raj submitted a complaint successfully.")

if __name__ == '__main__':
    make_complaint()