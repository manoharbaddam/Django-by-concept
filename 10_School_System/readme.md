# 🏫 Mini School System (Django)

**Project 10 – Bring It All Together**

A mini school management system built with **Django**, demonstrating role-based authentication, course management, and enrollments in a real-world–style project structure.

---

## 📌 Project Overview

This project simulates a **simple school system** with:

* Students
* Teachers
* Admins
* Courses (Classes)
* Enrollments

It is designed to **combine everything learned** in Django so far:
authentication, permissions, relationships, views, templates, and URL routing.

---

## 🎯 Key Objectives

* Build a real-world Django application
* Implement **custom user model**
* Apply **role-based permissions**
* Work with **ForeignKey & relational data**
* Practice clean project/app separation

---

## 🛠 Tech Stack

* **Python** 3.14+
* **Django** 6.0
* **SQLite** (development database)
* HTML + CSS (Django templates)
* Bootstrap-style UI (cards, dashboards)

---

## 📂 Project Structure

```text
.
├── config/                 # Project configuration (settings, urls, wsgi, asgi)
├── courses/                # Courses & enrollments app
│   ├── models.py           # Course & Enrollment models
│   ├── views.py            # Course views (list, enroll, dashboards)
│   ├── urls.py             # Course URL routing (namespaced)
│   ├── forms.py            # Forms for course creation
│   └── templates/          # Course-related templates
│
├── users/                  # Custom user & authentication app
│   ├── models.py           # CustomUser model
│   ├── views.py            # Login, registration, dashboards
│   ├── urls.py             # Auth & user URLs
│   └── templates/          # Login, registration, add user
│
├── templates/              # Global templates
│   └── dashboards/         # Role-based dashboards
│
├── static/                 # Static files (CSS)
├── db.sqlite3              # Development database
├── manage.py               # Django management script
└── README.md
```

---

## 👥 User Roles

The system uses a **custom user model** with roles:

* **ADMIN**
* **TEACHER**
* **STUDENT**

Roles control what each user can see and do in the system.

---

## 🧱 Core Models

### CustomUser

```text
- email (unique, used for login)
- role (STUDENT | TEACHER | ADMIN)
```

### Course

```text
- title
- description
- teacher (ForeignKey → CustomUser with role=TEACHER)
```

### Enrollment

```text
- student (ForeignKey → CustomUser with role=STUDENT)
- course (ForeignKey → Course)
- enrolled_date
- status (ACTIVE, COMPLETED, DROPPED)
```

---

## ✨ Features Implemented

### Admin

* Create users (students & teachers)
* Create courses
* Assign teachers to courses

### Student

* View available courses
* Enroll in courses
* View enrolled courses

### Teacher

* View assigned courses
* View list of students per course

---

## 🔐 Permissions & Access Control

* Only **admins** can create courses
* Only **students** can enroll
* Teachers can only see their own courses
* Students can only see their enrollments

All access is controlled using:

* User roles
* Login checks
* URL namespacing

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/manoharbaddam/Django-by-concept
cd 10_School_System
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install django
```

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the server

```bash
python manage.py runserver
```

Visit:
👉 `http://127.0.0.1:8000/`

---

## 🧪 Learning Outcomes

By completing this project, you practice:

✅ Custom user models

✅ Role-based permissions

✅ Complex ForeignKey relationships

✅ URL namespacing

✅ Django templates & dashboards

✅ Real-world app structure

---

## 🏁 Success Criteria

> **Success = You’ve built a working school system with real Django patterns**

If you understand **why** each part exists — you’re Django-ready 💪

---

## 📌 Future Improvements (Optional)

* Email verification
* Course completion tracking
* Pagination & search
* REST API (Django REST Framework)
* Deployment (Railway / Render)


