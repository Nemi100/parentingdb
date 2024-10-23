from werkzeug.security import generate_password_hash
from app import Admin, session_db  # Adjust import based on your structure

# Example admin registration
new_admin = Admin(email='admin@example.com', password=generate_password_hash('tekena'))
session_db.add(new_admin)
session_db.commit()
print("Admin added successfully!")
