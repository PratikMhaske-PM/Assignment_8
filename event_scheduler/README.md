# Event Scheduler - Django Web Application

A full-featured event scheduling web app built with Django as per Assignment 4.

## Features
- User Registration, Login, Logout
- Create, View, Update, Delete events (CRUD)
- Form validation with scheduling conflict detection
- Each user can only manage their own events

## Project Structure
```
event_scheduler/
├── event_scheduler/       # Project config (settings, urls)
├── events/                # Main app
│   ├── models.py          # Event model
│   ├── views.py           # List, Detail, Create, Update, Delete views
│   ├── forms.py           # EventForm with conflict validation
│   ├── urls.py            # App URL patterns
│   ├── auth_views.py      # Registration view
│   ├── auth_urls.py       # Auth URL patterns
│   └── templates/
│       ├── base.html
│       ├── events/        # event_list, detail, form, confirm_delete
│       └── registration/  # login, register
└── db.sqlite3
```

## Setup & Run

```bash
# 1. Install Django
pip install django

# 2. Apply migrations
python manage.py migrate

# 3. (Optional) Create superuser
python manage.py createsuperuser

# 4. Run server
python manage.py runserver

# Visit http://127.0.0.1:8000
```

## Event Model Fields
| Field        | Type          | Notes                   |
|-------------|---------------|-------------------------|
| user         | ForeignKey    | Links to Django User    |
| name         | CharField     | Event name              |
| date         | DateField     | Event date              |
| time         | TimeField     | Event time              |
| description  | TextField     | Optional description    |
| created_at   | DateTimeField | Auto set on create      |
| updated_at   | DateTimeField | Auto set on update      |
