
# 🛠️ Django Backend Assignment

A robust and secure Django backend system built with RESTful APIs, JWT Authentication, and Celery for handling asynchronous background tasks like sending emails. Ideal for showcasing real-world backend features in web development and system design.

---

## 📑 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Configuration](#environment-configuration)
- [Running the Project](#running-the-project)
- [API Usage](#api-usage)
- [Celery & Background Tasks](#celery--background-tasks)
- [Testing](#testing)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Features
- 🔐 JWT-based Authentication (`SimpleJWT`)
- 🔒 Protected API Endpoints
- 📨 Send Welcome Emails in Background using Celery
- 🧵 Async Worker using In-Memory Broker (Windows Friendly)
- 🗂️ Modular App Design (`core`, `users`, etc.)
- 🧪 Task Result Tracking (`django-celery-results`)
- 🔧 Easily Configurable & Scalable

---

## 💻 Technologies Used

| Component      | Tool/Library                     |
|----------------|----------------------------------|
| Backend        | Django, Django REST Framework    |
| Auth           | djangorestframework-simplejwt    |
| Tasks          | Celery, django-celery-results    |
| Broker         | In-memory (`memory://`)          |
| Database       | SQLite (default)                 |
| Language       | Python 3.11+                     |
| Environment    | Virtualenv                       |
| Testing        | DRF Browsable API, curl/Postman  |

---

## 🧱 Project Structure

```
django_backend/
│
├── core/                        # Application logic (tasks)
├── django_backend/             # Project settings
├── templates/                  # HTML templates (if any)
├── manage.py                   # Project runner
├── requirements.txt            # Dependencies
├── .env                        # Env vars (SECRET_KEY, etc.)
└── README.md                   # This file
```

---

## 🔧 Installation

### 1. Clone the Project
```bash
git clone https://github.com/yourusername/django-backend-assignment.git
cd django_backend
```

### 2. Create Virtual Environment
```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Migrate Database
```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

---

## ⚙️ Environment Configuration

Create a `.env` file in the project root:

```ini
DEBUG=True
SECRET_KEY='your-secret-key'
```
Update `settings.py` to load these with `python-decouple`.

---

## ▶️ Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

Start Celery worker (in a new terminal):

```bash
celery -A django_backend worker --pool=solo --loglevel=info
```

> Use `--pool=solo` for Windows compatibility.

---

## 🔐 API Usage

| Method | Endpoint              | Description                    |
|--------|-----------------------|--------------------------------|
| POST   | `/api/token/`         | Obtain access & refresh tokens |
| POST   | `/api/token/refresh/` | Refresh JWT access token       |
| GET    | `/api/private/`       | Protected welcome endpoint     |

**Authorization header:**
```
Authorization: Bearer <access_token>
```

---

## 📤 Celery & Background Tasks

In Django shell:

```bash
python manage.py shell
>>> from core.tasks import send_welcome_email
>>> send_welcome_email.delay("your_email@example.com")
```

Check the Celery terminal for logs.

---

## ✅ Testing

You can test protected API endpoints using curl or Postman:

Example:
```bash
curl -X GET http://127.0.0.1:8000/api/private/ \
     -H "Authorization: Bearer <access_token>"
```

You can also use Django’s test runner:

```bash
python manage.py test
```



## 🙌 Contributing

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m 'add feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit a pull request

---
