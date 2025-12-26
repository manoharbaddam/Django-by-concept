# 📔 Personal Journal App (User Registration Only)

## Overview

**Personal Journal App** is a beginner-plus level Django project focused on **user authentication** using Django’s built-in authentication system.

Users can **register, log in, and log out**, then create and view journal entries.  
At this stage, **journal entries are NOT user-specific** — all logged-in users can see all entries.  
This project is intentionally scoped to focus **only on authentication fundamentals**.

---

## Project Details

- **Primary Focus**: User Registration & Authentication  

---

## Core Learning Objective

> ✅ **Users can register and log in successfully.**  
That is the **only new requirement** compared to previous projects.

---

## Features (ONLY These)

- User registration page
- User login page
- User logout
- Add journal entries
- View all journal entries (shared visibility)
- Image upload with journal entry

❌ No user ownership  
❌ No permissions  
❌ No private journals  

---

## Tech Stack

- Python
- Django
- SQLite
- Django Authentication System
- HTML (Django Templates)
- CSS
- Media file handling (ImageField)

---

## Database Model

### JournalEntry

| Field | Type | Description |
|------|-----|-------------|
| title | CharField | Journal title |
| content | TextField | Journal content |
| image | ImageField | Optional image upload |
| created_at | DateTimeField | Auto timestamp |

---

## Project Structure

```

personal-journal/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3
├── media/
│   └── photos/
├── personalJournal/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       ├── index.html
│       ├── create_journal.html
│       ├── edit_journal.html
│       └── view_journal.html
├── static/
│   └── style.css
└── templates/
├── layout.html
└── registration/
├── login.html
├── logout.html
└── register.html

````

---

## Authentication Used

This project uses **Django’s default authentication system**:

- `django.contrib.auth.models.User`
- `UserCreationForm`
- `LoginView`
- `LogoutView`
- `@login_required` decorator
- Django authentication templates

📚 Official Documentation:
- https://docs.djangoproject.com/en/6.0/topics/auth/default/
- https://docs.djangoproject.com/en/6.0/ref/contrib/auth/#django.contrib.auth.models.User
- https://docs.djangoproject.com/en/6.0/topics/auth/passwords/

---

## Application Flow

| Action | Description |
|------|-------------|
| Register | Create a new user account |
| Login | Authenticate user |
| Logout | End session |
| Add Journal | Create a journal entry |
| View Journals | See all entries |

---

## Media Handling

- Images are uploaded via `ImageField`
- Files stored in `media/photos/`
- Used to practice Django file handling

---

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
````

---

### 2. Install Dependencies

```bash
python -m pip install Django Pillow
```

---

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4. Run Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## Success Criteria ✅

✔ Users can register 
✔ Users can log in
✔ Users can log out
✔ Logged-in users can create journal entries
✔ Images upload correctly

---

## Intentional Limitations

This project **intentionally does NOT include**:

* Entry ownership
* Permissions
* Private journals
* Role-based access

These will be introduced in later projects.

---

## Next Improvements (Future Projects)

* Associate journal entries with users
* Show only user’s own entries
* Profile pages
* Password reset
* Permissions & authorization
* REST API integration

---

## License

This project is for educational purposes and free to use or modify.

