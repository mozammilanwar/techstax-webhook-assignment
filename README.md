# 🧩 GitHub Webhook Event Viewer – TechStaX Internship Assignment

This project is a full-stack application that receives GitHub webhook events (Push, PR, Merge), stores them in MongoDB, and displays them live on a React frontend using a Flask backend.

---

## 📌 Features

✅ Webhook receiver endpoint (`/webhook`) using Flask  
✅ Stores GitHub event data (author, action, branches, timestamp)  
✅ MongoDB integration using `pymongo`  
✅ REST API to fetch stored events  
✅ React frontend with auto-refresh (every 15 seconds)  
✅ Clean UI to display GitHub actions in real-time  

---

## 🛠️ Tech Stack

- **Frontend**: React.js  
- **Backend**: Flask (Python)  
- **Database**: MongoDB (local instance)  
- **Other Tools**: Axios, Flask-CORS, Dotenv  

---

## 📁 Project Structure

```
techstax-webhook-task/
├── flask-backend/
│   ├── app.py
│   ├── .env
│   ├── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── EventList.js
│   │   ├── App.js
│   │   └── index.js
│   └── public/
├── .gitignore
├── README.md
```

---

## ⚙️ Setup Instructions

### 🔧 1. Backend (Flask)

```bash
cd flask-backend
python -m venv venv
venv\Scripts\activate      # For Windows
pip install -r requirements.txt
```

Create a `.env` file inside `flask-backend/` with:

```
MONGO_URI=mongodb://localhost:27017/
```

Then run the Flask server:

```bash
python app.py
```

✅ Server will start at: `http://localhost:5000`

---

### 💻 2. Frontend (React)

```bash
cd frontend
npm install
npm start
```

✅ UI will start at: `http://localhost:3000`

---

## 📦 API Endpoints

| Method | Endpoint      | Description           |
|--------|---------------|-----------------------|
| POST   | `/webhook`    | Receives GitHub event |
| GET    | `/events`     | Returns all events    |

---

## 🧪 Testing Webhook Locally

Use **Postman** or **curl** to test POST requests:

**URL:**  
```
http://localhost:5000/webhook
```

**Sample Payload:**
```json
{
  "author": "Mozammil",
  "actionType": "push",
  "fromBranch": "dev",
  "toBranch": "main"
}
```

---

## 📽️ GitHub Repo Link

🔗 [GitHub Repo](https://github.com/mozammilanwar/techstax-webhook-assignment)

---

## 👨‍💻 Author

**Mozammil Anwar**  
📧 mozammilanwar66@gmail.com

---

## 📝 Notes

This project is part of the **TechStaX Python Full-Stack Developer Internship Assessment**.  
It shows full integration of GitHub Webhook → Flask Backend → MongoDB → React UI with live updates.
