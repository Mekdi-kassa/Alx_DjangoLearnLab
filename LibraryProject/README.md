# LibraryProject

A Django-based library management system for managing books, users, and library operations.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

LibraryProject is a web-based library management system built with Django 5.2.3. This application provides a foundation for managing library resources, including books, members, and lending operations.

## ✨ Features

- **Django Admin Interface**: Built-in administrative interface for managing library data
- **User Authentication**: Secure user registration and login system
- **SQLite Database**: Lightweight database for development and small-scale deployments
- **Responsive Design**: Mobile-friendly interface (when templates are added)
- **Extensible Architecture**: Modular design for easy feature additions

## 📋 Requirements

- Python 3.8+
- Django 5.2.3
- SQLite (included with Python)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd LibraryProject
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django==5.2.3
```

### 4. Database Setup

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 🎯 Usage

### Accessing the Application

- **Main Application**: `http://127.0.0.1:8000/`
- **Admin Interface**: `http://127.0.0.1:8000/admin/`

### Admin Interface

The Django admin interface provides full CRUD operations for:
- User management
- Group permissions
- Session management
- Future library models (books, members, etc.)

## 📁 Project Structure

```
LibraryProject/
├── LibraryProject/          # Main project package
│   ├── __init__.py
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI configuration
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
└── README.md               # Project documentation
```

## ⚙️ Configuration

### Settings Overview

The project uses Django's default settings with the following key configurations:

- **Database**: SQLite (`db.sqlite3`)
- **Debug Mode**: Enabled (for development)
- **Time Zone**: UTC
- **Language**: English (US)
- **Static Files**: Served from `/static/` URL

### Environment Variables

For production deployment, consider setting:

```bash
export DJANGO_SECRET_KEY='your-secret-key-here'
export DJANGO_DEBUG=False
export DJANGO_ALLOWED_HOSTS='your-domain.com,www.your-domain.com'
```

## 🛠️ Development

### Running Tests

```bash
python manage.py test
```

### Creating Apps

To add new functionality, create Django apps:

```bash
python manage.py startapp books
python manage.py startapp members
python manage.py startapp lending
```

### Database Migrations

After making model changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files

For production:

```bash
python manage.py collectstatic
```

## 🔧 Common Commands

| Command | Description |
|---------|-------------|
| `python manage.py runserver` | Start development server |
| `python manage.py shell` | Open Django shell |
| `python manage.py dbshell` | Open database shell |
| `python manage.py check` | Check for project issues |
| `python manage.py showmigrations` | Show migration status |

## 🚀 Next Steps

To extend this library management system, consider adding:

1. **Book Management App**
   - Book models (title, author, ISBN, etc.)
   - Book catalog views
   - Search functionality

2. **Member Management App**
   - Member registration
   - Member profiles
   - Membership types

3. **Lending System App**
   - Book checkout/return
   - Due date tracking
   - Fine calculation

4. **Frontend Templates**
   - Bootstrap/CSS styling
   - User-friendly interfaces
   - Responsive design

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check Django documentation: https://docs.djangoproject.com/
- Django community: https://www.djangoproject.com/community/

---

**Note**: This is a development setup. For production deployment, ensure proper security configurations, environment variables, and server setup.