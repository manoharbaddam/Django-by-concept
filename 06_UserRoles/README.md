# 06_UserRoles – Simple Django User Roles Project

## 📌 Project Overview

This project demonstrates a **simple user roles system** using Django.

The main goal is to understand how to:
- Create a **custom user model**
- Add a **role field**
- Render **different dashboards** based on user roles

No advanced UI or permission framework is used.  
The project focuses only on **core role-based logic**.

---

## 🎯 Project Objectives

- Create a custom user model with roles
- Assign roles during registration
- Display different dashboards based on role
- Keep logic simple using if/else conditions

---

## 🧩 Roles Implemented

The application supports three user roles:

- **ADMIN**
- **MEMBER**
- **GUEST**

Each role sees a different dashboard page after login.

---

## 🗂 Project Structure

```

06_UserRoles
├── config/                 # Project configuration
├── myUserRoles/            # Main app
│   ├── models.py           # Custom user model with role field
│   ├── forms.py            # Registration and login forms
│   ├── views.py            # Authentication & role-based routing
│   ├── urls.py             # App URLs
│   └── templates/
│       └── Dashboards/
│           ├── admin_dashboard.html
│           ├── member_dashboard.html
│           └── guest_dashboard.html
├── templates/
│   ├── Registration/
│   │   ├── login_user.html
│   │   ├── logout_user.html
│   │   └── register_user.html
│   ├── index.html
│   └── layout.html
├── static/
│   └── css/
│       └── style.css
├── db.sqlite3
└── manage.py

````

---

## ⚙️ Features Implemented

- Custom user model using email as login field
- Role field using Django `choices`
- User registration and login
- Role-based dashboard rendering
- Simple template logic (`if/else`)
- Minimal UI (headings only for clarity)

---

## 🧠 What This Project Teaches

- How Django `choices` work in models
- How to access `request.user.role`
- Simple role-based logic in views and templates
- Custom user model fundamentals
- Keeping scope small and focused

---

## 🚀 How to Run the Project

1. Create a virtual environment
2. Install dependencies
3. Run migrations
4. Start the development server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
````

---

## ✅ Success Criteria

✔ Users have roles
✔ Roles are stored in the database
✔ Different users see different dashboards
✔ Logic is simple and readable

---


## 📘 Next Steps (Optional)

* Add role-based access restrictions
* Protect dashboards with decorators
* Improve UI styling
* Introduce Django permissions

---

### 🏁 Status: **Project Completed Successfully**


