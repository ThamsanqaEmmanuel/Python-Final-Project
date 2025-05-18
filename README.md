# Python-Final-Project
# Personal Finance Manager

A web-based personal finance management system built using Django, developed as part of a Financial Technology (FinTech) project. The goal is to help users manage their daily expenses, track financial habits, and work toward budgeting and saving goals.

---

## Project Inspiration

**Based on FinTech Project Idea #1**:

> **Personal Finance Management App** — Develop an app that helps users track expenses, set budgets, and manage finances effectively. Include features such as transaction categorization, budgeting tools, and financial goal setting.

---

##  Features

- Add daily expenses with title, amount, category, and date
- View a list of all recorded expenses
- See total expenditure summary
- Clean UI using HTML/CSS
- Secure form submission with CSRF protection

---

##  Technologies Used

- Python 3.13
- Django 5.2
- SQLite (default DB)
- HTML & CSS

---

##  Project Structure

financeproject/
├── financeproject/ # Django project config
│ └── settings.py
├── finance_app/ # Main app
│ ├── templates/
│ │ └── finance_app/
│ │ └── expense_list.html
│ ├── views.py
│ ├── models.py
│ ├── forms.py
│ └── urls.py
├── db.sqlite3
└── manage.py

yaml
Copy
Edit

---

##  Getting Started

1. **Clone the repo**

   git clone https://github.com/ThamsanqaEmmanuel/Python-Final-Project.git
   cd financeproject

Set up virtual environment



Install Django

pip install django

Run migrations

python manage.py migrate
Start the development server


python manage.py runserver
Open in browser
Visit: http://127.0.0.1:8000