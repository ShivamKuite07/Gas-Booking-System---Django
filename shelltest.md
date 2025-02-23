
---

## **Step 1: Open Django Shell**
Run the following command to open the Django shell:
```bash
python manage.py shell
```

---

## **Step 2: Test Cases for Cylinders**

### **1. Create Cylinders**
Create a few cylinders with different statuses:
```python
from core.models import Cylinder

# Create filled cylinders
Cylinder.objects.create(cylinder_id='CYL001', status='Filled')
Cylinder.objects.create(cylinder_id='CYL002', status='Filled')

# Create empty cylinders
Cylinder.objects.create(cylinder_id='CYL003', status='Empty')
Cylinder.objects.create(cylinder_id='CYL004', status='Empty')

# Verify cylinders
print(Cylinder.objects.all())
```

---

### **2. Assign a Cylinder to a User**
Assign a cylinder to a user:
```python
from core.models import User, Cylinder

# Get a user
user = User.objects.get(username='testuser')

# Get a filled cylinder
cylinder = Cylinder.objects.filter(status='Filled').first()

# Assign the cylinder to the user
cylinder.assigned_to = user
cylinder.status = 'Assigned'
cylinder.save()

# Verify the assignment
print(cylinder.assigned_to)  # Should return the user
print(cylinder.status)       # Should return 'Assigned'
```

---

### **3. Mark a Cylinder as Empty**
Mark a cylinder as empty after it’s returned by a user:
```python
from core.models import Cylinder

# Get an assigned cylinder
cylinder = Cylinder.objects.filter(status='Assigned').first()

# Mark it as empty
cylinder.status = 'Empty'
cylinder.assigned_to = None
cylinder.save()

# Verify the update
print(cylinder.status)  # Should return 'Empty'
```

---

## **Step 3: Test Cases for Bookings**

### **1. Create a Booking**
Create a booking for a user:
```python
from core.models import User, Cylinder, Booking

# Get a user and a filled cylinder
user = User.objects.get(username='testuser')
cylinder = Cylinder.objects.filter(status='Filled').first()

# Create a booking
booking = Booking.objects.create(user=user, cylinder=cylinder, status='Pending')

# Verify the booking
print(booking.user)       # Should return the user
print(booking.cylinder)   # Should return the cylinder
print(booking.status)     # Should return 'Pending'
```

---

### **2. Update Booking Status**
Update the status of a booking:
```python
from core.models import Booking

# Get a booking
booking = Booking.objects.filter(status='Pending').first()

# Update the status to 'Completed'
booking.status = 'Completed'
booking.save()

# Verify the update
print(booking.status)  # Should return 'Completed'
```

---

### **3. Cancel a Booking**
Cancel a booking:
```python
from core.models import Booking

# Get a booking
booking = Booking.objects.filter(status='Pending').first()

# Update the status to 'Cancelled'
booking.status = 'Cancelled'
booking.save()

# Verify the update
print(booking.status)  # Should return 'Cancelled'
```

---

## **Step 4: Test Cases for Complaints**

### **1. Create a Complaint**
Create a complaint for a user:
```python
from core.models import User, Complaint

# Get a user
user = User.objects.get(username='testuser')

# Create a complaint
complaint = Complaint.objects.create(
    user=user,
    issue_type='Gas Leak',
    description='Gas leak detected in the kitchen.',
    status='Pending'
)

# Verify the complaint
print(complaint.user)        # Should return the user
print(complaint.issue_type)  # Should return 'Gas Leak'
print(complaint.status)      # Should return 'Pending'
```

---

### **2. Update Complaint Status**
Update the status of a complaint:
```python
from core.models import Complaint

# Get a complaint
complaint = Complaint.objects.filter(status='Pending').first()

# Update the status to 'Completed'
complaint.status = 'Completed'
complaint.save()

# Verify the update
print(complaint.status)  # Should return 'Completed'
```

---

### **3. Cancel a Complaint**
Cancel a complaint:
```python
from core.models import Complaint

# Get a complaint
complaint = Complaint.objects.filter(status='Pending').first()

# Update the status to 'Cancelled'
complaint.status = 'Cancelled'
complaint.save()

# Verify the update
print(complaint.status)  # Should return 'Cancelled'
```

---

## **Step 5: Test Cases for Payments**

### **1. Create a Payment**
Create a payment for a booking:
```python
from core.models import User, Booking, Payment

# Get a user and a booking
user = User.objects.get(username='testuser')
booking = Booking.objects.filter(status='Completed').first()

# Create a payment
payment = Payment.objects.create(
    user=user,
    booking=booking,
    amount=1000.00,
    status='Success'
)

# Verify the payment
print(payment.user)       # Should return the user
print(payment.booking)    # Should return the booking
print(payment.amount)     # Should return 1000.00
print(payment.status)     # Should return 'Success'
```

---

### **2. Simulate a Failed Payment**
Simulate a failed payment:
```python
from core.models import Payment

# Get a payment
payment = Payment.objects.filter(status='Success').first()

# Update the status to 'Failed'
payment.status = 'Failed'
payment.save()

# Verify the update
print(payment.status)  # Should return 'Failed'
```

---

## **Step 6: Verify Data in Django Admin Panel**
1. Log in to the Django admin panel:
   ```
   http://127.0.0.1:8000/admin/
   ```
2. Verify that the test data (cylinders, bookings, complaints, payments) is visible and can be managed.

---

## **Step 7: Clean Up (Optional)**
If you want to clean up the test data, you can delete the objects:
```python
# Delete all cylinders
Cylinder.objects.all().delete()

# Delete all bookings
Booking.objects.all().delete()

# Delete all complaints
Complaint.objects.all().delete()

# Delete all payments
Payment.objects.all().delete()
```

---
