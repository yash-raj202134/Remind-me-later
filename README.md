# Remind-me-later

# 📆 Reminder API

This project is a simple **Django REST API** for managing reminders. Users can create, view, update, and delete reminders with fields such as date, time, message, and reminder type.

---

## 🚀 Features

- ✅ Create a reminder
- ✅ Read all or individual reminders
- ✅ Update a reminder
- ✅ Delete a reminder
- ✅ Validates input fields
- ✅ Clean and RESTful API responses

---

## 📦 Technologies Used

- Django
- Django REST Framework (DRF)
- SQLite (default)
- Python 3

---

## 🧩 Models

The `Reminder` model includes:

- `date` – Date of the reminder
- `time` – Time of the reminder
- `message` – Reminder message
- `reminder_type` – Either `SMS` or `Email`
- `created_at` – Timestamp when the reminder was created

---

## 🔌 API Endpoints

| Method | Endpoint | Description            |
|--------|----------|------------------------|
| POST   | `/api/reminders/` | Create a new reminder |
| GET    | `/api/reminders/` | List all reminders |
| GET    | `/api/reminders/<id>/` | Get a single reminder by ID |
| PUT    | `/api/reminders/<id>/` | Update a reminder |
| DELETE | `/api/reminders/<id>/` | Delete a reminder |

---

## 🛠 How to Use

1. **Clone the repo**

```bash
git clone https://github.com/yash-raj202134/Remind-me-later.git
cd Remind-me-later/remaind_me_later
```
2. **Install dependencies**

```bash
pip install -r requirements.txt
```
3. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```
4. **Run the server**
```bash
python manage.py runserver
```
5. **Test API using Postman or cURL**
    #### Sample request
```bash
POST /api/reminders/
Content-Type: application/json

{
  "date": "2025-05-14",
  "time": "10:00:00",
  "message": "Team standup meeting",
  "reminder_type": "SMS"
}
```