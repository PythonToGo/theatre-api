# Theatre Reservation API

> A RESTful API service for managing a theatre reservation system.  
> Built with **Django**, **Django REST Framework**, **PostgreSQL**, and **Docker**.

---

### 🔗 Live Demo

**https://theatre-api-9oy0.onrender.com/**  
**Swagger Docs**: https://theatre-api-9oy0.onrender.com/api/docs/   
**API Root**: https://theatre-api-9oy0.onrender.com/api/  
**API Actors**: https://theatre-api-9oy0.onrender.com/api/actors/  
**API Plays**: https://theatre-api-9oy0.onrender.com/api/plays/  
**API Reservations**: https://theatre-api-9oy0.onrender.com/api/reservations/  
**API Sample Ticket**: https://theatre-api-9oy0.onrender.com/api/reservations/1/tickets/  
**API Admin**: https://theatre-api-9oy0.onrender.com/admin/login/?next=/admin/  
![image](https://github.com/user-attachments/assets/63343e90-d5e3-4983-a2cb-105cbb35d3c5)  

---


## Branches Overview

| Branch | Description |
|--------|-------------|
| `main` | Local development with Docker + local PostgreSQL |
| `dev-dep` | Deployment-ready branch using [Neon](https://neon.tech) cloud PostgreSQL |

> Use `main` if you're running everything locally.  
> Use `dev-dep` to deploy to [Render](https://render.com) or other platforms with Neon.

---

## DB Structure
![alt text](image.png)

## Installing Using GitHub

```bash
git clone https://github.com/your-username/theatre-api.git
cd theatre-api
```
Then checkout the desired branch:
```bash
git checkout main  # For local PostgreSQL
# or 
git checkout dev-dep  # For Render + Neon
```



## Run with Docker

Make sure you have Docker and Docker Compose installed.
```bash
docker-compose up --build
```
The API will be available at: 
- http://localhost:8000/api/
- Swagger Docs: http://localhost:8000/api/docs/
- Redoc: http://localhost:8000/api/redoc/

##  Getting Access

1. Go to the admin panel: http://localhost:8000/admin/
2. Create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```
3. Use the superuser credentials to log in and manage models.

##  Features

- 🎭 Play Management: CRUD operations for Plays, Actors, Genres
- 🗓️ Performance Scheduling: Create performance slots in halls
- 🪑 Seat Selection: Users can select specific seat (row, seat) during reservation
- 📦 Nested API Support: Tickets under /reservations/{id}/tickets/
- 🔍 Filtering: Search Plays by title, filter Performances by date
- 🔑 Authentication: Users can only view their own reservations
- 📘 API Documentation: Automatically generated Swagger + ReDoc
- 🐳 Full Docker Support: Easy to deploy and run in containers

## Tech Stack

- Python 3.12
- Django 4.x
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- drf-yasg (Swagger docs)

## API Documentation

- Swagger UI: http://localhost:8000/api/docs/
- Redoc: http://localhost:8000/api/redoc/

## Author

Made by Taeyoung Kim 

## 
