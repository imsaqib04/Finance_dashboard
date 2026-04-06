# 📊 Finance Dashboard API

A robust, secure, and highly scalable RESTful API built with Django REST Framework (DRF) for managing financial records. This system features Role-Based Access Control (RBAC), real-time dashboard aggregations, automated API testing, and enterprise-grade security practices.

---

## ✨ Key Features

* **Role-Based Access Control (RBAC):**
  * `ADMIN`: Full CRUD access and User Management.
  * `ANALYST`: Read-only access to records and dashboard summaries.
  * `VIEWER`: Access restricted exclusively to the Dashboard Summary.
* **Authentication & Security:** Secured using JWT (JSON Web Tokens) for modern, stateless authentication. Includes extended user profiles (`first_name`, `last_name`).
* **Advanced Data Retrieval:** Built-in support for Pagination, Field Filtering (Date, Category, Type), Text Searching, and Column Ordering.
* **Dashboard Aggregation:** Real-time calculation of Total Income, Total Expense, Net Balance, and Category-wise breakdown via Django ORM aggregations.
* **Data Integrity & Audit:** Implemented "Soft Delete" functionality to preserve financial history and prevent accidental data loss.
* **API Security (Throttling):** Configured Rate Limiting to prevent API spam and DDoS attempts.
* **Interactive Documentation:** Fully integrated Swagger UI and exportable OpenAPI YAML specifications.
* **Automated Postman Testing:** Includes a pre-configured Postman collection with automated token-handling scripts.

---

## 🛠️ Tech Stack

* **Backend Framework:** Python 3, Django, Django REST Framework (DRF)
* **Database:** MySQL (Production ready) / SQLite (Local development)
* **Authentication:** `djangorestframework-simplejwt`
* **API Documentation:** `drf-yasg` (Swagger UI)
* **Data Parsing & Filtering:** `django-filter`

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/imsaqib04/Finance_dashboard.git](https://github.com/imsaqib04/Finance_dashboard.git)
cd Finance_dashboard
```

### 2. Set Up Virtual Environment
```bash
python -m venv env
# On Mac/Linux:
source env/bin/activate  
# On Windows:
env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup (MySQL)
Ensure MySQL is running on your machine. Create a database:
```sql
CREATE DATABASE finance_db;
```
*(Update your database credentials like USER and PASSWORD in `finance_backend/settings.py`)*.

### 5. Run Migrations & Create Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Start the Server
```bash
python manage.py runserver
```

---

## 📖 API Testing & Documentation

We have provided multiple ways to seamlessly explore and test this API:

### 1. Automated Postman Collection (Recommended ⚡)
A ready-to-use Postman collection (`Finance_Dashboard_API_Collection.json`) is included in the root directory. 
* **Pro-Tip:** The collection includes an automated **Post-response script**. When you hit the `Login` endpoint, it automatically extracts and saves the `access` and `refresh` tokens to your collection variables. You do not need to manually copy-paste tokens for subsequent requests!

### 2. Interactive Swagger UI
* **Live UI Docs:** `http://127.0.0.1:8000/api/docs/`
* **OpenAPI YAML:** You can download or view the raw `swagger.yaml` file included in this repository to import the API schema into your favorite client.
*(Note: To use secured endpoints in Swagger UI, login via the `/login/` endpoint, copy the `access` token, and click the **Authorize** button. Format: `Bearer <your_token>`)*

### 3. Django Admin Panel
* **Admin Dashboard:** `http://127.0.0.1:8000/admin/`
* Includes customized views to manage Users, Roles, and Financial Records through a secure GUI.

---

## 🔗 Core API Endpoints

* `POST /api/auth/register/` - Register a new user
* `POST /api/auth/login/` - Obtain JWT Access & Refresh tokens
* `POST /api/auth/refresh/` - Refresh expired access token
* `GET /api/records/` - List all records (Supports `?search=`, `?ordering=`, `?category=`, etc.)
* `POST /api/records/` - Create a new financial record
* `GET /api/dashboard/summary/` - Get real-time financial analytics
```
