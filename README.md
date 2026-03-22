# 🚀 Django Practicals

A complete Django project demonstrating multiple core concepts through practical lab experiments.

🔗 **Live Demo:** https://your-render-link.onrender.com
📂 **GitHub Repo:** https://github.com/04Priyanshuuuu/DjangoPracticals

---

## 📌 About the Project

This project is designed to showcase the implementation of various Django concepts through structured experiments. It covers everything from basic setup to authentication and blog functionality.

---

## 🧪 Experiments Covered

* **Experiment 1:** Create a simple Django project with one app and URL mapping
* **Experiment 2:** Student performance profile using models and views
* **Experiment 3:** Customize Django admin panel
* **Experiment 4:** Student registration form with validation
* **Experiment 5:** Blog application with posts, categories, and comments
* **Experiment 6:** User authentication (Signup, Login, Logout)
* **Experiment 7:** Multi-page website using templates and static files

---

## 🛠️ Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **Deployment:** Render

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/04Priyanshuuuu/DjangoPracticals.git
cd DjangoPracticals
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Run server

```bash
python manage.py runserver
```

---

## 🚀 Deployment (Render)

### Build Command:

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

### Start Command:

```bash
gunicorn DjangoPractical.wsgi
```

---

## 📁 Project Structure

```
DjangoPracticals/
│── DjangoPractical/
│── myapp/
│── blog/
│── registration/
│── templates/
│── static/
│── media/
│── manage.py
│── requirements.txt
│── Procfile
```

---

## 🔐 Features

✔ User Authentication (Login/Signup/Logout)
✔ Blog System (Posts, Categories, Comments)
✔ Django Admin Customization
✔ Form Validation
✔ Static & Media File Handling

---

## 📸 Screenshots

(Add your screenshots here after deployment)

---

## 👨‍💻 Author

**Priyanshu**
💡 Aspiring Developer | AI & Trading Enthusiast

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
