# 📚 FastAPI Books API

A clean FastAPI backend project to manage books using **PostgreSQL (Neon)** and **SQLAlchemy**.

This project started with in-memory storage and was later upgraded to a **real cloud database**, following industry-standard backend practices.

---

## 🚀 Features

- Get all books
- Get book by ID
- Add a new book
- Update book (PATCH)
- Delete book
- PostgreSQL database (Neon)
- SQLAlchemy ORM
- Dependency-based DB session management
- Proper HTTP status codes
- Pydantic validation

---

## 🛠 Tech Stack

- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL (Neon)**
- **Pydantic**
- **Uvicorn**

---

## 🗄 Database

This project uses **Neon (Serverless PostgreSQL)** as the database.

- Cloud-hosted PostgreSQL
- SSL-enabled connection
- Works like standard Postgres (no vendor lock-in)
- Connected via SQLAlchemy


---

📦 Installation & Setup

1️⃣ Clone the repository
git clone https://github.com/rajukola11/fastapi-books-crud.git
cd fastapi-books-crud

2️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the application
uvicorn app.main:app --reload


API will be available at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

