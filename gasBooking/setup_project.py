import subprocess

def run_script(script_name):
    """Run a Python script using subprocess."""
    try:
        print(f"Running {script_name}...")
        subprocess.run(['python', script_name], check=True)
        print(f"{script_name} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

def setup_project():
    # List of scripts to run
    scripts = [
        'empty_models.py',  # Empty models
        'create_admin.py',   # Create admin user
        'populate_cylinders.py',  # Populate cylinders
        'add_users.py',      # Add users (raj, rohan)
        'book_cylinders.py',  # Simulate cylinder bookings
        'make_complaint.py'  # Simulate complaint submission
    ]

    # Run each script
    for script in scripts:
        run_script(script)

    print("Project setup completed.")

if __name__ == '__main__':
    setup_project()