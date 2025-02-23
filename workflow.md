### **Complete Workflow of the Gas Utility System**  

This is a simple, **Django-based gas utility system** with an **admin panel, cylinder booking, complaint handling, and payment processing**. The logistics (delivery, tracking) are abstracted, focusing only on **inventory and user requests**.  

---

## **1️⃣ Core Features Overview**  
1. **Cylinder Booking (Primary Feature)**  
   - Users can book a cylinder online.  
   - The system automatically assigns a **filled cylinder** based on availability (**FIFO rule**).  
   - If the user is booking for the **first time**, they receive a new cylinder.  
   - If the user **already has a cylinder**, the old one is **marked empty** when they book a new one.  
   - Users **must pay ₹1000 per cylinder** (handled via a mock function `calling_razorpay()`).  
   - Each user can have **only one active cylinder at a time**.  

2. **Inventory Management**  
   - **Cylinders are tracked using unique IDs** (e.g., ABC123).  
   - Cylinders move through the following stages:  
     - **Filled Stock** → **Allocated to User** → **Returned as Empty** → **Refilled & Restocked**  
   - Admin can manually **mark cylinders as filled/empty** when needed.  
   - Admin needs to **manually refill empty cylinders** when they run out.
   - Admin can **manually assign cylinders** to specific users.  

3. **Complaints System**  
   - Users can **report issues** via a dropdown (e.g., **Gas Leak, Billing Issue, Regulator Issue, Other**).  
   - Users can **describe the issue** and submit a complaint.  
   - Users can **track complaint status** (Pending, Completed, Cancelled).  
   - Users can also **cancel their complaint** if needed.  
   - Admin can **update complaint statuses** in the admin panel.  

4. **Admin Panel & Controls**  
   - **Manage bookings and inventory** (mark cylinders as filled/empty, manually assign cylinders).  
   - **Handle complaints** (change statuses, resolve issues).  
   - **Override processes manually** if needed (e.g., force-assign a cylinder to a user).  

5. **Payments (Mock Razorpay)**  
   - Users **must pay ₹1000 per cylinder** before booking.  
   - We use a **mock function `calling_razorpay()`** that always returns **success** (simulating successful payment).  
   - In the future, **real Razorpay integration** can be added if needed.  

---

## **2️⃣ Detailed User Workflows**  

### **📌 1. Cylinder Booking Workflow**
| **Step** | **User Action** | **System Action** |  
|----------|---------------|------------------|  
| 🟢 **Step 1** | User logs in and clicks **"Book Cylinder"** | System checks if the user already has a cylinder |  
| 🟢 **Step 2** | If **first-time user**, proceed with new booking | System assigns a **filled cylinder** and generates an ID (e.g., ABC123) |  
| 🟢 **Step 3** | If **existing user**, system marks their **old cylinder as empty** before assigning a new one | Updates inventory: **Old cylinder → Empty, New cylinder → Assigned** |  
| 🟢 **Step 4** | User pays **₹1000** (mock payment function) | If successful, confirms the booking |  
| 🟢 **Step 5** | Booking complete 🎉 | User sees their assigned cylinder and booking details |  

---

### **📌 2. Complaint Handling Workflow**
| **Step** | **User Action** | **System/Admin Action** |  
|----------|---------------|------------------|  
| 🟠 **Step 1** | User clicks **"Report Issue"** | A dropdown appears with complaint types (**Gas Leak, Billing Issue, Other**) |  
| 🟠 **Step 2** | User selects a complaint type and enters a description | Complaint is stored with **status = Pending** |  
| 🟠 **Step 3** | User can check **complaint status** at any time | Status updates dynamically based on admin actions |  
| 🟠 **Step 4** | User can **cancel complaint** before admin processes it | Status changes to **Cancelled** |  
| 🟠 **Step 5** | Admin updates the complaint to **Completed, Cancelled, or Pending** | Status is updated in the user's dashboard |  

---

### **📌 3. Admin Workflow**
| **Step** | **Admin Action** | **System Impact** |  
|----------|---------------|------------------|  
| 🔴 **Step 1** | **View & manage bookings** | Assign, cancel, or override cylinder allocations |  
| 🔴 **Step 2** | **Manage cylinder inventory** | Mark cylinders as **filled or empty** |  
| 🔴 **Step 3** | **Handle complaints** | Change complaint status (Pending, Completed, Cancelled) |  
| 🔴 **Step 4** | **Manually assign a cylinder to a user** | Overrides auto-allocation rules |  
| 🔴 **Step 5** | **Resolve any system issues manually** | Ensures smooth operation |  

---

## **3️⃣ System Logic (Key Conditions & Rules)**  

✔ **Users can own only 1 cylinder at a time**  
✔ **First-time users get a new cylinder**  
✔ **Returning users get a new cylinder, and their old one is marked empty**  
✔ **Filled cylinders are allocated using FIFO (oldest stock first)**  
✔ **Admin can manually override any allocation or complaint**  
✔ **Payments must be successful (via `calling_razorpay()`) before booking is confirmed**  

---

## **4️⃣ Future Improvements & Enhancements**  
✅ **Real Razorpay integration** (replace `calling_razorpay()` with actual payment processing)  
✅ **More complaint tracking features** (notifications, auto-escalation)  
✅ **Enhanced admin dashboard** (visual analytics, better filters)  
✅ **Mobile app or API for integration with other services**  

---





### **Database Schema for the Gas Utility System**  
The database will have **5 core models**:  
1. **User** – Stores user details.  
2. **Cylinder** – Tracks each cylinder's status and unique ID.  
3. **Booking** – Stores cylinder booking details.  
4. **Complaint** – Manages complaints submitted by users.  
5. **Payment** – Tracks payments for cylinder bookings.  

---

## **1️⃣ User Model**  
Stores basic user details. Django’s built-in `User` model can be used, but we can extend it if needed.  

| **Field** | **Type** | **Description** |  
|-----------|---------|----------------|  
| `id` | AutoField (PK) | Unique identifier for the user |  
| `username` | CharField | Unique username |  
| `email` | EmailField | User email |  
| `phone` | CharField | Contact number | 
| `address` | TextField | Address |   
| `has_active_cylinder` | BooleanField | Indicates if user has a cylinder |  

---

## **2️⃣ Cylinder Model**  
Each cylinder has a **unique ID** and can be in different states.  

| **Field** | **Type** | **Description** |  
|-----------|---------|----------------|  
| `id` | AutoField (PK) | Unique identifier for the cylinder |  
| `cylinder_id` | CharField (Unique) | Unique ID (e.g., ABC123) |  
| `status` | CharField | **Choices: Filled, Empty, Assigned** |  
| `assigned_to` | ForeignKey (User, null=True) | User who currently has the cylinder |  

---

## **3️⃣ Booking Model**  
Handles cylinder bookings by users.  

| **Field** | **Type** | **Description** |  
|-----------|---------|----------------|  
| `id` | AutoField (PK) | Unique booking ID |  
| `user` | ForeignKey (User) | User making the booking |  
| `cylinder` | ForeignKey (Cylinder) | Cylinder assigned to user |  
| `booking_date` | DateTimeField | When the booking was made |  
| `status` | CharField | **Choices: Pending, Completed, Cancelled** |  

---

## **4️⃣ Complaint Model**  
Tracks issues reported by users.  

| **Field** | **Type** | **Description** |  
|-----------|---------|----------------|  
| `id` | AutoField (PK) | Unique complaint ID |  
| `user` | ForeignKey (User) | User who raised the complaint |  
| `issue_type` | CharField | Dropdown values (Gas Leak, Billing Issue, etc.) |  
| `description` | TextField | Additional details |  
| `status` | CharField | **Choices: Pending, Completed, Cancelled** |  
| `created_at` | DateTimeField | Timestamp of complaint submission |  

---

## **5️⃣ Payment Model**  
Stores transaction details for bookings.  

| **Field** | **Type** | **Description** |  
|-----------|---------|----------------|  
| `id` | AutoField (PK) | Unique transaction ID |  
| `user` | ForeignKey (User) | User making the payment |  
| `booking` | ForeignKey (Booking) | Associated booking |  
| `amount` | DecimalField | Payment amount (₹1000 per cylinder) |  
| `status` | CharField | **Choices: Success, Failed** |  
| `payment_date` | DateTimeField | When payment was processed |  

---

