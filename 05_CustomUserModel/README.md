# Custom User Model with Email Login (Django)

This project demonstrates how to create and use a **custom Django user model** that authenticates users using **email instead of username**.
It is built as a focused learning project to understand Django’s authentication system from the ground up.

---

## 🚀 Project Overview

**Goal:**
Create a Django project where:

* Users register using **email only**
* Users log in using **email + password**
* No `username` field exists
* Superuser creation works correctly
* Django admin works with the custom user

This project follows Django best practices by defining the custom user model **at project start**.

---

## 🧱 Tech Stack

* Python 3
* Django 6.0
* SQLite (development database)

---

## 📁 Project Structure

```
├── config/                 # Project configuration
│   ├── settings.py         # Django settings (AUTH_USER_MODEL defined here)
│   ├── urls.py             # Root URL configuration
│   └── wsgi.py / asgi.py
│
├── myCustomUser/           # Custom user app
│   ├── models.py           # CustomUser + CustomUserManager
│   ├── forms.py            # Registration & login forms
│   ├── views.py            # Auth views (register, login, logout)
│   ├── admin.py            # Admin integration
│   ├── urls.py             # App-level URLs
│   ├── templates/          # App templates
│   │   ├── register.html
│   │   ├── login_user.html
│   │   ├── logout_user.html
│   │   └── index.html
│   └── migrations/
│
├── templates/
│   └── layout.html         # Base layout
│
├── static/
│   └── style.css           # Basic styling
│
├── db.sqlite3
├── manage.py
```

---

## 👤 Custom User Model

The project uses a **custom user model** based on `AbstractBaseUser` and `PermissionsMixin`.

### Fields:

* `email` (unique, used for login)
* `first_name`
* `last_name` (optional)
* `is_active`
* `is_staff`
* `date_joined`

### Key Configuration:

```python
USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['first_name']
```

### Custom Manager:

* `create_user(email, password, **extra_fields)`
* `create_superuser(email, password, **extra_fields)`

---

## 🔐 Authentication Features

### ✅ Registration

* Users register using email and password
* Passwords are securely hashed using `set_password()`

### ✅ Login

* Users log in using **email + password**
* Django’s authentication system is used correctly

### ✅ Superuser

* Superusers are created with:

  ```bash
  python manage.py createsuperuser
  ```
* Email is used instead of username

### ✅ Admin Panel

* Custom users can be created and managed via `/admin/`

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/manoharbaddam/Django-by-concept.git
cd 05_CustomUserModel
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install django
```

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the server

```bash
python manage.py runserver
```

---

## 🧠 What This Project Teaches

* How Django authentication works internally
* Why custom user models must be created at project start
* How `AbstractBaseUser` differs from `AbstractUser`
* How forms, models, and database constraints interact
* Secure password handling
* Email-based authentication design

---

## 📌 Why Create a Custom User Early?

Django tightly couples the user model with:

* Migrations
* Foreign keys
* Authentication
* Permissions

Changing it later is risky and expensive.
This project demonstrates the **correct approach from day one**.

---

## 🎯 Project Status

✅ Custom user model implemented
✅ Email-based login
✅ Registration flow complete
✅ Superuser creation works
✅ Admin integration complete

**Project Complete ✔**

---

## 🔜 Possible Next Steps

* Email verification
* Password reset via email
* User profile extension
* Custom authentication backend
* Role-based permissions

---

## 📜 License

This project is for educational purposes.

---
