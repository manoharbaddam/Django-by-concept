# 📒 NotesApp – Basic CRUD Application (Django)

## Overview

**NotesApp** is a beginner-friendly Django web application that demonstrates the core **CRUD operations** (Create, Read, Update, Delete).  
The application allows users to manage notes without authentication or user separation, making it ideal for learning Django fundamentals.

---

## Features

- List all notes
- Create a new note
- View a single note
- Edit an existing note
- Delete a note

---

## Tech Stack

- Python
- Django
- SQLite (default Django database)
- HTML (Django Templates)

---

## Project Structure

```

notesApp/
├── README.md
├── config/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3
├── notes/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── notes/
│           ├── index.html
│           ├── create_note.html
│           ├── view_note.html
│           ├── edit_note.html
│           └── delete_note.html
└── templates/
└── layout.html

````

---

## Model

### Note

| Field | Type | Description |
|------|------|-------------|
| title | CharField | Title of the note |
| content | TextField | Note content |
| created_at | DateTimeField | Auto-generated timestamp |

---

## Installation & Setup

### 1. Create Virtual Environment

```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
````

---

### 2. Install Dependencies

```bash
python -m pip install Django
python -m django --version
```

---

### 3. Create Project & App

```bash
django-admin startproject config notesApp
cd notesApp
python manage.py startapp notes
```

Add the app to `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'notes.apps.NotesConfig',
]
```

---

## Database Setup

Run migrations to create database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Application Flow

| Action      | URL             | Description        |
| ----------- | --------------- | ------------------ |
| List Notes  | `/`             | Displays all notes |
| Create Note | `/create/`      | Add a new note     |
| View Note   | `/<id>/view`    | View note details  |
| Edit Note   | `/<id>/edit/`   | Update note        |
| Delete Note | `/<id>/delete/` | Remove note        |

---

## Templates

* `layout.html` – Base template
* `index.html` – List all notes
* `create_note.html` – Create form
* `view_note.html` – Note details
* `edit_note.html` – Edit form
* `delete_note.html` – Delete confirmation

All templates extend `layout.html` to maintain consistent UI.

---

## Running the Application

```bash
python manage.py runserver
```

Open browser and visit:

```
http://127.0.0.1:8000/
```

---

## Purpose of the Project

This project is designed to help beginners understand:

* Django project structure
* Models and ORM
* Forms and validation
* Function-based views
* URL routing
* Template inheritance
* CRUD operations

---

## Future Improvements

* User authentication
* Note ownership
* Pagination
* Search functionality
* Class-based views
* REST API with Django REST Framework

---

## License

This project is for educational purposes and is free to use and modify.
