# Django REST API

A RESTful API built with Django REST Framework for managing courses and related entities. This project serves as a learning example for building APIs with DRF.

## 🚀 Features

- RESTful API endpoints
- Django REST Framework integration
- SQLite database (can be configured for PostgreSQL)
- Admin interface for data management
- Custom API models and serializers

## 🛠️ Tech Stack

- **Backend Framework:** Django 4.2+
- **API Framework:** Django REST Framework 3.14+
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **Authentication:** (To be implemented)
- **Deployment Ready:** Configured for Render deployment

## 📋 Prerequisites

- Python 3.9+
- pip (Python package manager)
- Git

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/AndreyGOIT/django-rest-api.git
cd django-rest-api
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

```bash
# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## 📁 Project Structure

```
django-rest-api/
├── config/                 # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL routing
│   └── wsgi.py           # WSGI configuration
├── courses/               # Courses app
│   ├── models.py         # Database models
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # API views
│   ├── urls.py           # App URL routing
│   └── admin.py          # Admin configuration
├── venv/                  # Virtual environment
├── requirements.txt       # Project dependencies
└── manage.py             # Django management script
```

## 🌐 API Endpoints

| Endpoint             | Method | Description              |
| -------------------- | ------ | ------------------------ |
| `/api/courses/`      | GET    | List all courses         |
| `/api/courses/`      | POST   | Create new course        |
| `/api/courses/{id}/` | GET    | Retrieve specific course |
| `/api/courses/{id}/` | PUT    | Update specific course   |
| `/api/courses/{id}/` | DELETE | Delete specific course   |
| `/admin/`            | GET    | Django admin interface   |

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
```

## 🚀 Deployment

This project is configured for deployment on Render:

1. Connect your GitHub repository to Render
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python manage.py runserver 0.0.0.0:8000`
4. Add environment variables in Render dashboard

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

## 📝 License

This project is licensed under the MIT License.

## 📧 Contact

Andrey Erokhin - [GitHub](https://github.com/AndreyGOIT)

Project Link: [https://github.com/AndreyGOIT/django-rest-api](https://github.com/AndreyGOIT/django-rest-api)

---

## 🎯 Next Steps

- [ ] Add user authentication
- [ ] Implement pagination
- [ ] Add filtering and search
- [ ] Write comprehensive tests
- [ ] Add API documentation with Swagger

---
