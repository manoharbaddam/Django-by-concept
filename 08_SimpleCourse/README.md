# Project 8: Simple Course Platform (Many-to-Many Intro)

A simple Django project to understand and practice **ManyToManyField** relationships by building a basic course enrollment system.

---

## 📌 Project Overview

In this project, **students can enroll in multiple courses**, view their enrolled courses, and unenroll at any time.

The main goal is to **learn and master Django’s `ManyToManyField`** through a practical, real-world example.

---

## ⏱ Duration
**4–5 days**

## ⭐ Difficulty
**Intermediate**

## 🎯 Core Focus
- Django `ManyToManyField`
- Relationship management (`add`, `remove`)
- Forward & reverse relationships

---

## 🛠 Tech Stack

- Python 3
- Django
- SQLite (default Django DB)
- HTML / CSS
- Django Templates

---

## 📂 Project Structure

```

08_SimpleCourse/
├── config/              # Project settings
├── courses/             # Course-related logic
├── userApp/             # Authentication & Student model
├── templates/           # Global templates
├── static/               # CSS files
├── db.sqlite3
├── manage.py
└── README.md

````

---

## 🧩 Models

### Course
```python
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
````

### Student (Custom User Extension)

```python
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_courses = models.ManyToManyField(Course, blank=True)
```

---

## 🚀 Features Implemented

✅ List all available courses

✅ Student can enroll in a course

✅ Student can view enrolled courses

✅ Student can unenroll from a course

✅ Admin dashboard to view course enrollments

✅ Superuser-only dashboard access

---

## 🔁 Many-to-Many Operations Used

### Enroll a student

```python
student.enrolled_courses.add(course)
```

### Unenroll a student

```python
student.enrolled_courses.remove(course)
```

### Get enrolled courses

```python
student.enrolled_courses.all()
```

### Get students in a course (reverse relation)

```python
course.student_set.all()
```

---

## 🔐 Authentication & Authorization

* Custom student profile linked to Django `User`
* Login / Register / Logout
* Dashboard restricted to **superusers only**
* Navbar dynamically changes based on authentication & role

---

## 🧪 Admin Dashboard

* Lists all courses
* Shows students enrolled in each course
* Accessible only by **superusers**

---

## 📥 Seeding Courses (Optional)

A custom Django management command is included:

```bash
python manage.py seed_courses
```

This loads sample courses from `courses.json`.

---

## ▶️ How to Run the Project

1. Clone the repository
2. Create virtual environment

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies

   ```bash
   pip install django
   ```
4. Apply migrations

   ```bash
   python manage.py migrate
   ```
5. Create superuser

   ```bash
   python manage.py createsuperuser
   ```
6. Run server

   ```bash
   python manage.py runserver
   ```

---

## ✅ Success Criteria

🎉 **Project is successful if:**

* Students can enroll & unenroll from courses
* Many-to-many relationships work correctly
* Reverse relationships are accessible
* Admin can view enrollments

---

## 📚 What You Learned

✔ ManyToManyField fundamentals
✔ Forward & reverse relationships
✔ Django ORM relationship methods
✔ Template conditionals for enrollment logic
✔ Access control using `is_superuser`

---

## 🧠 Next Improvements (Optional)

* Add course categories
* Pagination for courses
* AJAX-based enroll/unenroll
* Course capacity limits
* Permissions instead of `is_superuser`

---

Happy Coding 🚀
**This project builds a strong foundation for advanced Django relationships.**

