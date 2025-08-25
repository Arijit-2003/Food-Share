# Food-Share
📌 Overview: 
Food Share is a platform that connects food donors with NGOs and needy people. The goal is to reduce food wastage by enabling restaurants, households, and organizations to donate excess food safely and efficiently.

✨ Features
👤 User Roles: Donors, NGOs/Receivers, and Admins.

🍴 Food Donation: Donors can post available food details (quantity, type, pickup location).

🔔 Notifications: Real-time updates when new donations are available.

📊 Admin Dashboard: Manage users, donations, and reports.

🔒 Authentication: Secure login and registration.


Food Share is a platform that connects food donors with NGOs and needy people. The goal is to reduce food wastage by enabling restaurants, households, and organizations to donate excess food safely and efficiently.

🛠️ Tech Stack

Backend Framework: Django (Python)

Database: SQLite (default) / MySQL / PostgreSQL

Frontend: Django Templates (customized with HTML, CSS, Bootstrap)

Authentication: Django Auth System


📂 Project Structure (Example)
FoodShare/

│── foodshare/        # Main Django project folder (settings, urls, wsgi)

│── donations/        # App handling food donation logic

│── users/            # App handling authentication and user roles

│── templates/        # HTML templates

│── static/           # CSS, JS, images

│── manage.py         # Django management file

│── requirements.txt  # Project dependencies

│── README.md         # Documentation

🚀 Getting Started
1️⃣ Clone the repository

git clone https://github.com/your-username/FoodShare.git

cd FoodShare

2️⃣ Create and activate a virtual environment

python -m venv venv

venv\Scripts\activate   # On Windows

source venv/bin/activate  # On Mac/Linux

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run migrations

python manage.py migrate

5️⃣ Create a superuser (for admin access)

python manage.py createsuperuser

6️⃣ Run the development server

python manage.py runserver


Visit 👉 http://127.0.0.1:8000/ in your browser.

👨‍💻 Author
Arijit Karmakar

