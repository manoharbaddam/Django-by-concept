# 📚 Course Enrollment System (Many-to-Many Through Model)

A Django project demonstrating how to model and manage **many-to-many relationships with extra data** using a **through model**.  
This project tracks **when students enroll in courses** and the **status of each enrollment**.

---

## 🚀 Project Overview

In real-world applications like Learning Management Systems (LMS), subscriptions, or memberships, relationships often need **extra fields**.

This project solves that problem by using a **ManyToMany relationship with a custom through model**.

---

## 🎯 Core Features

- ✅ Enroll students in courses
- 📅 Track enrollment date automatically
- 🔄 Update enrollment status (Active / Completed / Dropped)
- 🧾 View enrollment history for each course
- 🔐 Admin-only access to enrollment history

---

## 🧠 Key Concepts Covered

- ManyToMany relationships with `through`
- Storing metadata on relationships
- Querying through models efficiently
- Updating related objects safely
- Role-based access control in templates and views

---

## 🗂 Models

### Course
```python
- title (CharField)
- description (TextField)
````

### Student (Custom User)

```python
- courses (ManyToManyField → Course, through='Enrollment')
```

### Enrollment (Through Model)

```python
- student (ForeignKey → Student)
- course (ForeignKey → Course)
- enrolled_date (DateTimeField, auto_now_add=True)
- status (CharField: ACTIVE, COMPLETED, DROPPED)
```

Each `Enrollment` represents **one student enrolled in one course**.

---

## 🔁 Enrollment Status Flow

* `ACTIVE` → Student is currently enrolled
* `COMPLETED` → Student finished the course
* `DROPPED` → Student unenrolled or stopped

---

## 🖥 User Features

### Student

* View enrolled courses
* See enrollment date
* Update enrollment status via dropdown

### Admin / Superuser

* View enrollment history per course
* See all students, dates, and statuses

---

## 🔐 Access Control

* Enrollment history pages are restricted to:

  * `is_superuser` users
* Views are protected with decorators
* Templates hide admin-only links from normal users

---

## 🧪 Sample Queries

### Enroll a Student

```python
Enrollment.objects.create(
    student=request.user,
    course=course
)
```

### Get Student Enrollment History

```python
Enrollment.objects.filter(student=request.user)
```

### Get Course Enrollment History

```python
Enrollment.objects.filter(course=course)
```

### Count Active Students in a Course

```python
Enrollment.objects.filter(
    course=course,
    status='ACTIVE'
).count()
```

---

## ⚙️ Tech Stack

* Python
* Django
* Django Templates
* SQLite (default, easily swappable)

---

## 🛠 Installation

```bash
git clone <repo-url>
cd course-enrollment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📈 What This Project Demonstrates

* Real-world Django data modeling
* Clean separation of concerns
* Secure data updates using POST requests
* Proper use of Django ORM
* Production-ready patterns

---

## 📌 Future Improvements

* Add completed date
* Pagination for enrollment history
* Filters by status
* REST API using Django REST Framework
* AJAX-based status updates

---

## 👨‍💻 Author 

Built as part of a Django backend learning series focused on **real-world patterns** and **scalable design**.

---

## ⭐ Final Note

> If you understand this project, you understand **one of the most important Django ORM patterns**.

This pattern appears in:

* LMS platforms
* Subscriptions
* E-commerce orders
* Membership systems
* Role-based access control

