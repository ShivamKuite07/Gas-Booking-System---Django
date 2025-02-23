from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    # Additional fields
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    isAdmin = models.BooleanField(default=False)
    has_active_cylinder = models.BooleanField(default=False)

    def __str__(self):
        return self.username


User = get_user_model()

class Cylinder(models.Model):
    STATUS_CHOICES = [
        ('Filled', 'Filled'),
        ('Empty', 'Empty'),
        ('Assigned', 'Assigned'),
    ]

    cylinder_id = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Filled')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.cylinder_id} - {self.status}"



class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cylinder = models.ForeignKey(Cylinder, on_delete=models.SET_NULL, null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"

    @staticmethod
    def assign_pending_bookings():
        # Get the oldest pending booking
        pending_booking = Booking.objects.filter(status='Pending').order_by('booking_date').first()
        if pending_booking:
            # Check for available filled cylinders
            filled_cylinder = Cylinder.objects.filter(status='Filled').first()
            if filled_cylinder:
                # Assign the cylinder and mark booking as completed
                pending_booking.cylinder = filled_cylinder
                pending_booking.status = 'Completed'
                pending_booking.save()

                # Update the cylinder status
                filled_cylinder.status = 'Assigned'
                filled_cylinder.assigned_to = pending_booking.user
                filled_cylinder.save()



# Signal to assign pending bookings when a cylinder is marked as filled
@receiver(post_save, sender=Cylinder)
def assign_pending_bookings_on_cylinder_update(sender, instance, **kwargs):
    if instance.status == 'Filled':
        Booking.assign_pending_bookings()





class Complaint(models.Model):
    ISSUE_TYPES = [
        ('Gas Leak', 'Gas Leak'),
        ('Billing Issue', 'Billing Issue'),
        ('Regulator Issue', 'Regulator Issue'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPES)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint {self.id} by {self.user.username}"

class Payment(models.Model):
    STATUS_CHOICES = [
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Success')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} for Booking {self.booking.id}"