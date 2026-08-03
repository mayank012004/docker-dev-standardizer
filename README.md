# 🐳 Docker-Based Development Environment Standardizer

> A Dockerized Student Management System built using Django and PostgreSQL to demonstrate how Docker Compose creates a standardized development environment and eliminates the "Works on My Machine" problem.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-6.0-success?logo=django)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql)
![License](https://img.shields.io/badge/License-Educational-green)

---

# 📖 Project Overview

This project demonstrates how Docker can be used to standardize development environments across different systems.

Instead of installing Python, Django, PostgreSQL and other dependencies manually on every developer's computer, everything runs inside Docker containers.

The project implements a **Student Management System** where users can:

- Add students
- View students
- Edit student information
- Delete students

The application uses:

- Django for backend
- PostgreSQL as database
- Docker Compose for container orchestration

---

# 🎯 Objectives

- Standardize development environments
- Eliminate dependency conflicts
- Solve the "Works on My Machine" problem
- Learn Docker containerization
- Learn Django web development
- Learn PostgreSQL integration
- Understand Docker Compose networking

---

# ✨ Features

- ✅ Add Student
- ✅ Display Student List
- ✅ Edit Student Details
- ✅ Delete Student
- ✅ PostgreSQL Database
- ✅ Dockerized Application
- ✅ Responsive Bootstrap UI
- ✅ Django Admin Panel

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Programming Language |
| Django 6 | Web Framework |
| PostgreSQL | Database |
| Docker | Containerization |
| Docker Compose | Multi-container Management |
| Bootstrap 5 | Frontend Styling |
| HTML5 | Frontend |
| CSS3 | Styling |

---

# 📂 Project Structure

```
docker-dev-standardizer/
│
├── Dockerfile
├── docker-compose.yml
├── README.md
│
└── app/
    ├── manage.py
    ├── config/
    │
    ├── students/
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   ├── templates/
    │   │
    │   └── migrations/
    │
    └── db.sqlite3
```

---

# 🏗️ Architecture

```
                User
                  │
                  ▼
           Browser (localhost:8000)
                  │
                  ▼
          Docker Container
          Django Application
                  │
                  ▼
          PostgreSQL Container
                  │
                  ▼
             Student Database
```

---

# ⚙️ Docker Architecture

```
+--------------------------------------+
|          Docker Compose              |
+--------------------------------------+
          │                 │
          ▼                 ▼
+----------------+   +------------------+
| Django         |   | PostgreSQL       |
| Container      |<->| Container        |
| Port : 8000    |   | Port : 5432      |
+----------------+   +------------------+
```

---

# 🗄️ Database Design

Student Table

| Field | Type |
|--------|------|
| id | Integer |
| name | CharField |
| roll_number | Integer |
| department | CharField |

---

# 🚀 How to Run

## Clone Repository

```bash
git clone https://github.com/mayank012004/docker-dev-standardizer.git
```

---

## Go inside project

```bash
cd docker-dev-standardizer
```

---

## Start Docker

```bash
docker compose up
```

---

## Open Browser

```
http://localhost:8000
```

---

# 📷 Screenshots

## Home Page

(Add Screenshot Here)

---

## Student List

(Add Screenshot Here)

---

## Edit Student

(Add Screenshot Here)

---

## Django Admin

(Add Screenshot Here)

---

# 🧠 Challenges Faced

### 1. Django App Not Detected

Problem:

- Students app wasn't recognized.

Solution:

- Added `'students'` to `INSTALLED_APPS`.

---

### 2. TemplateDoesNotExist Error

Problem:

```
TemplateDoesNotExist
```

Solution:

- Created proper template folder structure:

```
students/
    templates/
        students/
            index.html
```

---

### 3. URL Routing Issue

Problem:

Django couldn't find application URLs.

Solution:

Configured:

```
config/urls.py
```

and

```
students/urls.py
```

correctly.

---

### 4. Permission Denied

Problem:

VS Code couldn't save files.

Solution:

Corrected file permissions and edited files from the appropriate project directory.

---

### 5. Duplicate Roll Number Error

Problem:

```
IntegrityError
```

Solution:

Deleted duplicate records from the database and ensured unique roll numbers.

---

### 6. Git Authentication Failed

Problem:

GitHub no longer accepts passwords.

Solution:

Generated a Personal Access Token (PAT) and authenticated Git securely.

---

# 📚 Learning Outcomes

Through this project, I learned:

- Docker Basics
- Docker Containers
- Docker Compose
- Container Networking
- Volume Mounting
- Environment Standardization
- Django MVC Architecture
- Django ORM
- CRUD Operations
- PostgreSQL Integration
- Git Version Control
- GitHub Repository Management

---

# 🔮 Future Enhancements

- Student Login
- Authentication
- Search Student
- Pagination
- Profile Picture Upload
- REST API
- Docker Swarm Deployment
- Kubernetes Deployment
- CI/CD Pipeline using GitHub Actions

---

# 👨‍💻 Author

**Mayank Singh Bora**

B.Tech CSE (Cloud Computing & Virtualization Technology)

UPES, Dehradun

GitHub:

https://github.com/mayank012004

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.
