import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, abort, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import random
import string
from functools import wraps

app = Flask(__name__)

# Configurations
app.secret_key = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Dictionary to store file codes
file_codes = {}

def generate_unique_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login_register'))
        return f(*args, **kwargs)
    return decorated_function

# Route for login and register page
@app.route('/')
def login_register():
    return render_template('loginregister.html')

# Register route
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        flash('Username or Email already exists. Please log in.', 'danger')
        return redirect(url_for('login_register'))

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    flash('Registration successful! Please log in.', 'success')
    return redirect(url_for('login_register'))

# Login route
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        flash(f'Welcome back, {user.username}!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Invalid email or password. Please try again.', 'danger')
        return redirect(url_for('login_register'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login_register'))

# File upload route
@app.route('/upload', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part', 400
        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400
        if file:
            filename = file.filename
            code = generate_unique_code()
            while code in file_codes:
                code = generate_unique_code()
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], code + '_' + filename)
            file.save(file_path)
            file_codes[code] = file_path
            return render_template('success.html', code=code)
    return render_template('index.html')

# File download route
@app.route('/download', methods=['GET', 'POST'])
@login_required
def download():
    if request.method == 'POST':
        code = request.form['code']
        if code in file_codes:
            try:
                return send_file(file_codes[code], as_attachment=True)
            except FileNotFoundError:
                del file_codes[code]
                return render_template('error.html'), 404
        else:
            return render_template('error.html'), 404
    return render_template('download.html')

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)