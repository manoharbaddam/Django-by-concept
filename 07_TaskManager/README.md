# 🗂️ Task Manager (One-to-Many Practice)

A beginner-friendly Django project focused on mastering **ForeignKey relationships**, **custom users**, and **one-to-many data modeling**.

This project demonstrates how **tasks belong to projects**, and **projects belong to users**.

---

## 📌 Project Overview

This Task Manager allows users to:
- Create projects
- Add tasks under projects
- Assign tasks to users
- Mark tasks as completed
- View tasks grouped by project

The main goal of this project is to **solidify relational thinking in Django ORM**.

---

## 🎯 Learning Objectives

This project helped practice:

- ✅ One-to-Many relationships
- ✅ Multiple `ForeignKey`s in a single model
- ✅ Custom User integration
- ✅ `related_name` usage (`project.tasks.all()`)
- ✅ Chained relationships (`task.project.owner`)
- ✅ Filtering queries using multiple fields
- ✅ Safe form handling with user-based filtering

---

## 🧱 Data Models

### Project
| Field | Type |
|-----|-----|
| name | CharField |
| owner | ForeignKey → CustomUser |

### Task
| Field | Type |
|-----|-----|
| title | CharField |
| project | ForeignKey → Project |
| assigned_to | ForeignKey → CustomUser |
| completed | BooleanField |

---

## 🛠️ Features

- 🔐 Authentication-protected views
- 📁 Project creation per user
- 📝 Task creation inside projects
- 👤 Assign tasks to users
- ✅ Mark tasks as complete/incomplete
- 🔍 View tasks filtered by project

---

## 🧩 Key Relationships

```python
project.tasks.all()        # Get all tasks for a project
task.project.owner         # Get project owner from task
user.tasks.all()           # Tasks assigned to a user
user.owned_projects.all()  # Projects owned by a user
````

---

## 🚀 Setup Instructions

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd task-manager
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install django
   ```

4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

---

## 🔒 Security Considerations

* All task and project views are restricted to logged-in users
* Projects are filtered by owner
* Tasks are filtered by their associated project and user

---

## 📈 Possible Improvements

* Add permissions (only project owners can edit tasks)
* Use class-based views
* Add task deadlines and priorities
* Add pagination for large task lists
* Improve UI with frontend framework

---

## 🏁 Conclusion

This project serves as a strong foundation for understanding **Django relational modeling** and **real-world ORM usage**.

> **Success = Tasks belong to projects, projects belong to users**

---

## 🧑‍💻 Author
B.Manohar Reddy

Built as part of Django practice to strengthen backend fundamentals.
