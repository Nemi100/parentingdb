

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Routes](#routes)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [License](#license)
10. [Contributing](#contributing)
11. [Contact](#contact)

## Introduction
A website for parents boosting an admin login for CRUD operations on the career page.


## Features
- Admin login/logout
- Job posting management (CRUD operations)
- Flash messages for success/error notifications
- Secure password handling

## Requirements
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

2. **Create and activate virtual environment.

2. **Install dependencies.(Check Requirements).

2. **Create Database.(i used postgres).

## Usage
1. **Run the application.(python app.py).

2. **Access the application and go to your localhost: http://localhost:5000/.

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

**Admin login:
- At the /admin/login
- valid and invalid credentials can be entered to validate proper data handling

**Job Postings:
- 
- valid and invalid credentials can be entered to validate proper data handling





     

