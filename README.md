```markdown
# 📊 Finance Dashboard API

A robust, secure, and highly scalable RESTful API built with Django REST Framework (DRF) for managing financial records. This system features Role-Based Access Control (RBAC), real-time dashboard aggregations, and enterprise-grade security practices.

---

## ✨ Key Features

* **Role-Based Access Control (RBAC):**
  * `ADMIN`: Full CRUD access and User Management.
  * `ANALYST`: Read-only access to records and dashboard summaries.
  * `VIEWER`: Access restricted exclusively to the Dashboard Summary.
* **Authentication & Security:** Secured using JWT (JSON Web Tokens) for modern, stateless authentication.
* **Advanced Data Retrieval:** Built-in support for Pagination (10 items/page), Field Filtering (Date, Category, Type), Text Searching, and Column Ordering.
* **Dashboard Aggregation:** Real-time calculation of Total Income, Total Expense, Net Balance, and Category-wise breakdown.
* **Data Integrity:** Implemented "Soft Delete" functionality to prevent accidental data loss, along with strict Backend Model validations (e.g., blocking negative amounts and future dates).
* **API Security (Throttling):** Configured Rate Limiting to prevent API spam and DDoS attempts.
* **Interactive Documentation:** Fully integrated Swagger UI for seamless API testing and exploration.
* **Custom Admin Panel:** Enhanced Django Admin interface featuring a custom HTML Proxy Model to visualize analytics directly in the backend.
* **Automated Data Seeding:** Python script included to instantly populate the database with realistic dummy data for testing.

---

## 🛠️ Tech Stack

* **Backend Framework:** Python 3, Django, Django REST Framework (DRF)
* **Database:** MySQL (Configured for Production) / SQLite (for quick dev)
* **Authentication:** `djangorestframework-simplejwt`
* **API Documentation:** `drf-yasg` (Swagger UI)
* **Data Parsing & Filtering:** `django-filter`

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/finance_backend.git](https://github.com/yourusername/finance_backend.git)
cd finance_backend
```

### 2. Set Up Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Note: If `requirements.txt` is missing, manually install `django`, `djangorestframework`, `djangorestframework-simplejwt`, `django-filter`, `pymysql`, `drf-yasg`)*

### 4. Database Setup (MySQL)
Ensure MySQL is running on your machine. Create a database:
```sql
CREATE DATABASE finance_db;
```
Update your database credentials (USER, PASSWORD) in `finance_backend/settings.py`.

### 5. Run Migrations & Create Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Seed Dummy Data (Optional but Recommended)
Populate your database with realistic records to test the dashboard instantly:
```bash
python seed_data.py
```

### 7. Start the Server
```bash
python manage.py runserver
```

---

## 📖 API Endpoints & Testing

The easiest way to test the API is through the built-in Swagger interface.

* **Swagger UI / API Docs:** `http://127.0.0.1:8000/api/docs/`
* **Django Admin Panel:** `http://127.0.0.1:8000/admin/`

### Core Routes:
* `POST /api/auth/register/` - Register a new user (Auto-assigned to Viewer role)
* `POST /api/auth/login/` - Obtain JWT Access & Refresh tokens
* `GET /api/records/` - List all records (Supports `?search=`, `?ordering=`, `?category=`)
* `POST /api/records/` - Create a new financial record
* `GET /api/dashboard/summary/` - Get real-time financial analytics

*(Note: To use secured endpoints in Swagger, login via the `/login/` endpoint, copy the `access` token, and click the **Authorize** button at the top of the Swagger page. Format: `Bearer <your_token>`)*
```

### Final Git Push:
README file ko save karne ke baad apna aakhiri push kar dijiye:
```bash
git add README.md
git commit -m "docs: added professional README for project setup and details"
git push origin main
```
