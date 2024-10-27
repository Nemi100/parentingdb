

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Routes](#routes)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [admin_dashboard](#admin_dashboard)
10. [base](#base)
11. [index](#index)
12. [career](#career)
13. [admin_login](#admin_login)
14. [Contributing](#contributing)
15. [Contact](#contact)

## Introduction
A website for parents boosting an admin login for CRUD operations on the career page.


## Features
- Admin login/logout
- Job posting management (CRUD operations)
- Flash messages for success/error notifications
- Secure password handling

## Technologies
- Python 3.7+
- Flask
- SQLAlchemy
- psycopg2
- Jinja2
- Werkzeug

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nemi100/parentingdb.git
   cd parentingdb

2. **Create and activate virtual environment**:
   python -m venv venv
   venv/bin/activate

2. **Install dependencies**:
   pip install  (Check Requirements)

2. Create Database.(i used postgres).

## Usage
1. **Run the application**:
   python app.py

2. Access the application and go to your localhost: http://localhost:5000/.

## Routes

- /: Main page
- /career: Careers page displaying job postings
- /admin/login: Admin login page
- /admin/dashboard: Admin dashboard for managing job postings (protected)
- /admin/logout: Admin logout
- /admin/job: Add job posting (POST)
- /admin/job/<int:id>: Modify or delete job posting (POST)

## Testing

## Manuel Testing

1.Admin login:
- At the /admin/login
- valid and invalid credentials can be entered to validate proper data handling

2.Job Postings:
- Loging in will help navigate to /admin/dashboard/
- valid and invalid credentials can be entered to validate proper data handling

### Form Testing
| Element                         | Action        | Expected Result                         | Pass/Fail |
|---------------------------------|---------------|-----------------------------------------|-----------|
| Username                        | Text input    | Text displayed to user                  | Pass      |
| Password                        | Text input    | Password is hidden to user              | Pass      |
| Show password icon              | Click         | Password is unveiled to user            | Pass      |
| Login button (fields correct)   | Click         | Redirect to Homepage                    | Pass      |
| Login button (fields incorrect) | Click         | Reload login page                       | Pass      |
| Error message (fields incorrect)|               | Error message to user                   | Pass      |
| Login button (Username not found)| Click        | Reload login page, error message to user | Pass      |
| Login button (Password incorrect)| Click        | Reload login page, error message to user | Pass      |
| Redirect Link 'Register Now'    | Click         | Redirect to Register page               | Pass      |


## Contact
For any questions, please contact:
-Name: Tekena Nemi
-Email: teksity@gmail.com


     

