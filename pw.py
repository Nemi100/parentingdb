from werkzeug.security import generate_password_hash
from app import Admin, session_db  

# Example admin registration with user input
email = input("Enter admin email: ")
password = input("Enter admin password: ")

new_admin = Admin(email=email, password=generate_password_hash(password))
session_db.add(new_admin)
session_db.commit()
print("Admin added successfully!")
