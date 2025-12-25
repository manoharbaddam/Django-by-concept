# 📒 Category-Based Notes App (Django)

## Overview

**Category-Based Notes App** is a beginner-level Django project that extends a basic Notes CRUD application by introducing **categories** using a **ForeignKey (One-to-Many) relationship**.

Each note belongs to a category, allowing notes to be organized and filtered efficiently.

---

## Project Details

- **Core Focus**: One-to-Many relationship using `ForeignKey`

---

## Features

- Create and manage categories
- Assign a category to each note
- Select categories using a dropdown when creating notes
- View notes filtered by category
- Display category name with each note

---

## Tech Stack

- Python
- Django
- SQLite
- HTML (Django Templates)

---

## Database Models

### Category

| Field | Type | Description |
|------|------|-------------|
| name | CharField | Name of the category |

---

### Note

| Field | Type | Description |
|------|------|-------------|
| title | CharField | Title of the note |
| content | TextField | Note content |
| category | ForeignKey | Links note to a category |
| created_at | DateTimeField | Auto timestamp |

---

## Relationship

```

Category (1) ──────── (Many) Notes

```

Each **Category** can have multiple **Notes**, but each **Note** belongs to only one **Category**.

---

## Project Structure

```

notesApp/
├── README.md
├── config/
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
│           ├── delete_note.html
│           ├── category_list.html
│           └── create_category.html
└── templates/
└── layout.html

````

---

## Key Learning Outcomes

This project helps you understand:

✅ One-to-Many relationships using `ForeignKey`  
✅ Creating related models  
✅ Using dropdowns with `ModelChoiceField`  
✅ Filtering QuerySets  
```python
Note.objects.filter(category=selected_category)
````

✅ Accessing related data

```python
note.category.name
```

---

## Application Flow

| Action          | Description                   |
| --------------- | ----------------------------- |
| Create Category | Add new categories            |
| Create Note     | Select category from dropdown |
| View Notes      | Display notes with category   |
| Filter Notes    | Show notes by category        |

---

## Running the Project

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

---

### 2. Install Dependencies

```bash
python -m pip install Django
```

---

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4. Start Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## Success Criteria ✅

✔ Notes are linked to categories
✔ Categories appear in dropdown while creating notes
✔ Notes can be filtered by category
✔ Category name is displayed with each note

---

## Future Improvements

* Category-wise note count
* Edit & delete categories
* User-based categories
* Search notes within categories
* Convert to Class-Based Views
* REST API using Django REST Framework

---

## License

This project is created for educational purposes and is free to use and modify.

