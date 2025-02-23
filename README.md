
---

### Read workflow.md to understand the project structure and workflow.

### Steps to Set Up the Project

1. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

2. **Run the Setup Script**:
   Use the `setup_project.py` script to set up the project with test data. This script will:
   - Empty all models (for fresh start).
   - Create an admin user.
   - Populate cylinders (6 filled, 4 empty).
   - Add two users (`raj` and `rohan`).
   - Simulate cylinder bookings for `raj` and `rohan`.
   - Simulate a complaint submission by `raj`.

   Run the script:
   ```bash
   python setup_project.py
   ```

3. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

4. **Access the Application**:
   - Open your browser and go to `http://127.0.0.1:8000/`.
   - Log in as:
     - **Admin**: Username: `admin`, Password: `123`
     - **User**: Username: `raj` or `rohan`, Password: `123` 

5. **Note**:
   - This is just for basic setup.
   - You can add more users and simulate more scenarios as needed.
   - Everytime we run the setup_project.py script, it will empty all the models and then recreate them with the new data. This is done to ensure a fresh start for each run.

---

