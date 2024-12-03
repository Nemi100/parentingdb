import os
from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
from sqlalchemy import create_engine, Column, Integer, String, Text, MetaData, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'tekena#')

# Database setup
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg2://")
engine = create_engine(DATABASE_URL)
Base = declarative_base()
metadata = MetaData()

#Admin model
class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)  



# Job model
class Job(Base):
    __tablename__ = 'job'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    salary = Column(Float, nullable=True)
    location = Column(String(100), nullable=True)
    admin_id = Column(Integer, ForeignKey('admin.id'))
    admin = relationship('Admin', back_populates='jobs')

Admin.jobs = relationship('Job', order_by=Job.id, back_populates='admin')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session_db = Session()

# Create initial admin if not exists
initial_admin_email = 'admin@example.com'
initial_admin_password = 'tekena#'

admin_exists = session_db.query(Admin).filter_by(email=initial_admin_email).first()
if not admin_exists:
    new_admin = Admin(email=initial_admin_email, password=generate_password_hash(initial_admin_password))
    session_db.add(new_admin)
    session_db.commit()
    print("Initial admin created successfully!")
          
@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/career')
def career():
    jobs = session_db.query(Job).all()
    return render_template('career.html', jobs=jobs)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        admin = session_db.query(Admin).filter_by(email=email).first()
        if admin and check_password_hash(admin.password, password):
            session['admin_logged_in'] = True
            session['admin_id'] = admin.id  
            return redirect(url_for('admin_dashboard'))
        flash('Invalid credentials.', 'error')
        return redirect(url_for('admin_login'))
    return render_template('admin_login.html')

@app.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        new_admin = Admin(email=email, password=hashed_password)
        session_db.add(new_admin)
        session_db.commit()
        flash('Admin registered successfully.', 'success')
        return redirect(url_for('admin_login'))
    return render_template('admin_register.html')


@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    jobs = session_db.query(Job).all()
    return render_template('admin_dashboard.html', jobs=jobs)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))


@app.route('/admin/job', methods=['POST'])
def add_job():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    title = request.form['title']
    description = request.form['description']
    salary = request.form['salary']
    location = request.form['location']
    admin_id = session.get('admin_id') 
    new_job = Job(title=title, description=description, salary=salary, location=location, admin_id=admin_id)
    session_db.add(new_job)
    session_db.commit()
    flash('Job added successfully.', 'success')
    return redirect(url_for('admin_dashboard'))

def update_job(id):
    title = request.form['title']
    description = request.form['description']
    salary = request.form['salary']
    location = request.form['location']
    job = session_db.query(Job).filter_by(id=id).first()
    if job is None:
        flash('Job not found.', 'error')
        return redirect(url_for('admin_dashboard'))
    job.title = title
    job.description = description
    job.salary = salary
    job.location = location
    session_db.commit()
    flash('Job updated successfully.', 'success')
    return redirect(url_for('admin_dashboard'))



@app.route('/admin/job/<int:id>', methods=['POST'])
def modify_job(id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    method = request.form.get('_method')
    if method == 'PUT':
        return update_job(id)
    elif method == 'DELETE':
        return delete_job(id)
    return jsonify({'message': 'Invalid method'}), 405


def delete_job(id):
    job = session_db.query(Job).filter_by(id=id).first()
    if job is None:
        return jsonify({'message': 'Job not found'}), 404
    session_db.delete(job)
    session_db.commit()
    return redirect(url_for('admin_dashboard'))                            




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)                         