# 🎓 AI-Based Student Performance Analytics System

A web-based student performance analytics system built with **Django** and **Machine Learning**. Predicts pass/fail, academic grade, and dropout risk for each student using Logistic Regression and Decision Tree algorithms.

🚀 **Live Demo** → https://faraaz.pythonanywhere.com

---

## ✨ Features

- 🔐 Secure session-based admin login
- 📋 Full CRUD — Add, Edit, Delete student records
- 🤖 ML Predictions — Pass/Fail, Grade (A/B/C), Dropout Risk
- 💡 Auto suggestions for low attendance students
- 📊 Interactive charts — Bar, Pie, Scatter (Chart.js)
- 🏆 Top 5 performers & weakest students panel
- 🗄️ SQLite database with Django ORM

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.x, Django 4.2 |
| Database | SQLite 3 |
| Machine Learning | scikit-learn, numpy |
| Frontend | HTML5, CSS3, Chart.js |

---

## 📁 Folder Structure

```
student_analytics/
├── app/
│   ├── templates/
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   └── add_student.html
│   ├── static/
│   │   └── style.css
│   ├── models.py        # Student DB model
│   ├── views.py         # All view functions
│   ├── urls.py          # URL routing
│   └── ml_model.py      # ML training & predictions
├── student_analytics/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── seed_data.py         # Load sample students
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/MOHD-FARAZ-01/Ai-based-student-analytics-app.git
cd Ai-based-student-analytics-app
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate --run-syncdb
```

### 5. Load sample data
```bash
python seed_data.py
```

### 6. Start server
```bash
python manage.py runserver
```

### 7. Open in browser
```
http://127.0.0.1:8000
```

---

## 🔑 Login Credentials

```
Username : admin
Password : admin123
```

---

## 🤖 ML Predictions Logic

| Prediction | Algorithm | Criteria |
|-----------|-----------|----------|
| Pass / Fail | Logistic Regression | marks + attendance pattern |
| Grade A/B/C | Decision Tree | A=80+, B=60-79, C=below 60 |
| Dropout Risk | Logistic Regression | low marks + low attendance |
| Suggestion | Rule-based | attendance < 50% |

---

## 👨‍💻 Developer

**Mohd. Faraz** — BCA VI Semester  
Feroze Gandhi Institute of Professional Studies

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
