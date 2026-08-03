<div align="center">

# 🐳 Docker-Based Development Environment Standardizer

### Student Management System using Django, PostgreSQL & Docker Compose

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Django-6.0-success?style=for-the-badge&logo=django">
<img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql">
<img src="https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker">

---

A Dockerized Student Management System demonstrating how Docker Compose creates a standardized development environment and solves the **"Works on My Machine"** problem.

</div>

---

# 📖 Project Description

This project demonstrates how Docker Compose standardizes development environments by containerizing a Django application with PostgreSQL.

Instead of installing Python, Django, PostgreSQL, and other dependencies on every developer's machine, the application runs inside Docker containers.

This ensures every developer works in an identical environment regardless of operating system.

---

# 🎯 Objectives

- Standardize development environments
- Eliminate dependency conflicts
- Learn Docker & Docker Compose
- Understand Django architecture
- Integrate PostgreSQL with Django
- Perform CRUD operations
- Deploy applications consistently

---

# ✨ Features

✅ Add Student

✅ View Students

✅ Edit Student

✅ Delete Student

✅ PostgreSQL Database

✅ Dockerized Environment

✅ Bootstrap User Interface

✅ Django Admin Panel

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Programming Language |
| Django 6 | Backend Framework |
| PostgreSQL | Database |
| Docker | Containerization |
| Docker Compose | Multi-container Management |
| Bootstrap | Frontend UI |
| HTML/CSS | Interface |
| Git | Version Control |
| GitHub | Code Hosting |

---

# 🏗 System Architecture

```
             User
               │
               ▼
       Web Browser
               │
               ▼
      Django Container
               │
               ▼
     PostgreSQL Container
               │
               ▼
          Student Database
```

---

# 🐳 Docker Architecture

```
+-------------------------------------+
|          Docker Compose             |
+-------------------------------------+
         │                 │
         ▼                 ▼

+-----------------+   +-------------------+
| Django Container|   | PostgreSQL        |
| Port : 8000     |   | Port : 5432       |
+-----------------+   +-------------------+
```

---

# 📂 Project Structure

```
docker-dev-standardizer
│
├── Dockerfile
├── docker-compose.yml
├── README.md
│
└── app
    │
    ├── manage.py
    │
    ├── config
    │      settings.py
    │      urls.py
    │
    └── students
           │
           ├── models.py
           ├── views.py
           ├── urls.py
           ├── admin.py
           ├── migrations
           │
           └── templates
                 └── students
                        index.html
                        edit.html
```

---

# 🗄 Database Schema

Student Table

| Field | Type |
|--------|------|
| ID | Integer |
| Name | CharField |
| Roll Number | Integer |
| Department | CharField |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/mayank012004/docker-dev-standardizer.git
```

Move into the project

```bash
cd docker-dev-standardizer
```

Start Docker

```bash
docker compose up
```

Visit

```
http://localhost:8000
```

---

# 📷 Screenshots

## Home Page

_Add screenshot here_

---

## Student List

_Add screenshot here_

---

## Edit Student

_Add screenshot here_

---

## Django Admin

_Add screenshot here_

---

# ⚡ Challenges Faced

### 1. Django App Not Detected

✔ Added students app in INSTALLED_APPS.

---

### 2. TemplateDoesNotExist Error

✔ Corrected template directory structure.

---

### 3. URL Routing Issue

✔ Configured project and application URLs.

---

### 4. File Permission Error

✔ Fixed Linux file permissions.

---

### 5. Duplicate Roll Number

✔ Removed duplicate records and maintained unique roll numbers.

---

### 6. GitHub Authentication

✔ Used Personal Access Token (PAT) instead of password.

---

# 📚 Learning Outcomes

- Docker Basics
- Docker Compose
- Container Networking
- PostgreSQL Integration
- Django ORM
- CRUD Operations
- Git Version Control
- GitHub Workflow
- Linux Commands

---

# 🔮 Future Enhancements

- Authentication
- Student Login
- Search Functionality
- REST API
- Docker Swarm
- Kubernetes Deployment
- CI/CD Pipeline
- Cloud Deployment (AWS)

---

# 👨‍💻 Author

**Mayank Singh Bora**

B.Tech Computer Science Engineering

UPES, Dehradun

GitHub:

https://github.com/mayank012004

---

<div align="center">

### ⭐ If you found this project useful, please consider giving it a Star ⭐

</div>
