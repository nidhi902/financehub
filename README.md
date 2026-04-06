# 💰 Finance Hub API

## 📌 Project Overview

Finance Hub is a Django REST API-based backend system designed to manage financial records with **role-based access control (RBAC)** and **dashboard analytics**.

The system ensures secure data access where users can only interact with data according to their roles.

---

## 🧠 System Design (Backend Structure)

The project follows a clean backend structure:

* Models → Data representation (Financedata, Profile)
* Serializers → Data validation & transformation
* Views → Business logic & role-based access
* URLs → API routing

---

## 👥 User Roles & Access Control

### 👤 Viewer (User)

* Can create financial records
* Can view only their own data

### 📊 Analyst

* Can view all data
* Can update/edit records

### 👑 Admin

* Full access (create, update, delete)
* Can manage and control all users' data

---

## 🔐 Authentication

* Token-based authentication is implemented using DRF
* Users must include token in headers:

```
Authorization: Token your_token
```

---

## 🔗 API Endpoints

### 🔹 Authentication

* POST /signup/
* POST /login/

---

### 🔹 Finance APIs

* GET /financedata/finance/ → Role-based data retrieval
* POST /financedata/finance/ → Create record
* PUT /financedata/finance/<id>/ → Update (Admin/Analyst)
* DELETE /financedata/finance/<id>/ → Admin only
Note: All endpoints are protected and require token authentication except signup and login.
---

## 📊 Dashboard API

* GET /dashboard/
  The dashboard API returns aggregated data instead of raw records, reducing client-side computation.

### Provides:

* Total Income
* Total Expenses
* Net Balance
* Category-wise aggregation
* Recent transactions

---

## 🧠 Business Logic

* Data ownership enforced using `uploaded_by`
* Role-based filtering:

  * Admin/Analyst → All data
  * User → Own data only
* Dashboard uses aggregation functions (`Sum`) for insights

---

## 🗄️ Database Design

### Financedata Model:

* title
* description
* amount
* category
* uploaded_by (ForeignKey)
* uploaded_at

👉 This ensures proper **data ownership and relational integrity**

---

## ⚠️ Validation & Error Handling

* Invalid login → returns error
* Unauthorized access → 403 Forbidden
* Missing token → 401 Unauthorized
* Data validation handled via serializers
Proper HTTP status codes (200, 201, 400, 401, 403) are used for responses.
---

## 🧪 Testing(using postman)

1. Signup a new user → `POST /signup/`
2. Login → `POST /login/`
3. Copy token from response
4. Add header:
   Authorization: Token your_token
5. Test Finance APIs
6. Test Dashboard API

---

## ⚙️ Setup Instructions

```
git clone <repo>
cd project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 💡 Additional Thoughtfulness

* Role-based dashboard (same API, different output)
* Clean separation of concerns
* Scalable design for future enhancements (e.g., admin creating for other users)

---

## 🎯 Conclusion

This project demonstrates:

* Secure authentication
* Role-based authorization
* Data ownership
* Aggregated analytics

---

## 👨‍💻 Author

Nidhi Gautam
