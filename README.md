# Recipe Sharing Website (Django)

A simple Django web app for sharing recipes.

## Features
- User profiles (Profile model with avatar)
- Recipe creation (title, description, ingredients, instructions, cook time, photo)
- Categories and tags
- Ratings (1–5) and comments
- Admin panel for managing all data

## Tech
- Python 3.14
- Django 6.0
- SQLite (default)
- Pillow (for image upload)

## How to run (Windows)
```bat
cd mysite
python -m venv venv
venv\Scripts\activate
pip install django pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver