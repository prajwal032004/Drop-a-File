# Drop-a-File📥📁📤
A secure and user-friendly web application built with Flask that enables authenticated users to share files using unique codes. The application features user authentication, secure file uploads, and a code-based file retrieval system.

---
## 🔗Link

[live website view ](https://prajwalab.pythonanywhere.com/)

---
## 🚀 Features

- **User Authentication**
  - Secure registration and login system
  - Password hashing for enhanced security
  - Session management for authenticated users

- **File Management**
  - Secure file upload system
  - Unique code generation for each uploaded file
  - Size limit enforcement (16MB per file)
  - Code-based file retrieval system

- **Security Features**
  - Password hashing using PBKDF2-SHA256
  - Protected routes with login requirement
  - Secure session management
  - File size restrictions

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Security**: Werkzeug Security for password hashing
- **Frontend**: HTML/CSS (Templates)

## 📋 Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

## 🔧 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/secure-file-sharing.git
   cd secure-file-sharing
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

5. Initialize the database:
   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

6. Run the application:
   ```bash
   python app.py
   ```

The application will be available at `http://localhost:5000`

## 🔒 Security Considerations

- The application uses secure password hashing
- File uploads are restricted to 16MB
- Authentication is required for file operations
- Unique codes are generated for file sharing

## 📁 Project Structure

```
secure-file-sharing/
├── app.py                 # Main application file
├── uploads/              # File upload directory
├── templates/            # HTML templates
│   ├── index.html
│   ├── loginregister.html
│   ├── download.html
│   ├── success.html
│   └── error.html
├── static/              # Static files (CSS, JS)   
└── README.md           # Project documentation
```

## ⚙️ Requirements

```plaintext
Flask==2.2.3
Flask-SQLAlchemy==2.5.1
Werkzeug==2.2.3
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Self License.

## 👥 Authors

-[Prajwal](https://github.com/prajwal032004)

## 🙏 Acknowledgments

- Flask documentation and community
- SQLAlchemy documentation
- Python community

### ✨️Happy Coding