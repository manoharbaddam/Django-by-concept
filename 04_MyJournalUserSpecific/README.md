# 📓 My Journal – User-Specific Journal App (Django)

## Overview

**My Journal** is a beginner-plus Django project that builds on user authentication by introducing **user-specific content ownership**.

Each registered user can create journal entries that are **private to their account**.  
Users can **only view, edit, and delete their own journal entries**, ensuring proper ownership and access control.

This project focuses strictly on **linking content to users** using Django’s `User` model.

---

## Project Details


- **Difficulty**: ⭐⭐ Beginner+  


---

## Core Learning Objective

> ✅ **Each user has their own private journal.**

---

## Features (ONLY These)

- Automatically assign journal author to logged-in user
- Display only the current user’s journal entries
- Prevent users from editing or deleting others’ entries
- Create, view, edit, and delete personal journal entries
- Image upload support

❌ No sharing  
❌ No admin-level permissions  
❌ No advanced roles  

---

## Tech Stack

- Python
- Django
- SQLite
- Django Authentication System
- HTML (Django Templates)
- CSS
- Media file handling

---

## Database Model

### JournalEntry

| Field | Type | Description |
|------|-----|-------------|
| title | CharField | Entry title |
| content | TextField | Entry content |
| author | ForeignKey (User) | Owner of the entry |
| image | ImageField | Optional image |
| created_at | DateTimeField | Auto timestamp |

---

## Relationship

```

User (1) ──────── (Many) Journal Entries

```

Each journal entry belongs to **one user**, and each user can have **many entries**.

---

## Project Structure

```

my-journal/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3
├── media/
│   └── images/
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
│       ├── user_journal.html
│       ├── create_journal.html
│       ├── edit_journal.html
│       ├── delete_journal.html
│       └── view_journal.html
└── templates/
├── layout.html
└── registration/
├── login.html
├── logout.html
└── register.html

````

---

## Key Concepts Practiced

✅ ForeignKey to Django `User` model  
✅ `request.user` in views  
✅ Filtering QuerySets by user  

```python
JournalEntry.objects.filter(author=request.user)
````

✅ Ownership validation

```python
if entry.author != request.user:
    return redirect("user-journal")
```

✅ Automatic author assignment

```python
entry.author = request.user
```

---

## Application Flow

| Action        | Description            |
| ------------- | ---------------------- |
| Register      | Create user account    |
| Login         | Authenticate user      |
| Create Entry  | Auto-assign author     |
| View Journals | Only own entries shown |
| Edit/Delete   | Allowed only for owner |

---

## Media Handling

* Images uploaded via `ImageField`
* Stored in `media/images/`
* Used for file handling practice

---

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

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

Visit:

```
http://127.0.0.1:8000/
```

---

## Success Criteria ✅

✔ Users can register and log in
✔ Journal entries are linked to users
✔ Users see only their own entries
✔ Users cannot edit/delete others’ entries
✔ Images upload successfully

---

## Intentional Scope Limitations

This project **does NOT include**:

* Sharing journals
* Admin moderation
* Groups or permissions
* Public profiles

These are reserved for future projects.

---

## Next Possible Enhancements

* Public/private journal toggle
* Journal sharing
* Category tagging
* Pagination
* REST API with DRF
* User profile pages

---


## License

This project is created for learning purposes and is free to use or modify.
