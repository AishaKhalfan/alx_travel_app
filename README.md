# alx_travel_app
Milestone 1: Setup and Database Configuration
ALX Travel App
A Django REST API for travel listings management.
Features

Travel listings API
User authentication
Swagger API documentation
Celery for asynchronous tasks with RabbitMQ
MySQL database integration

Setup Instructions
Prerequisites

Python 3.8+
MySQL
RabbitMQ
Redis (for Celery results backend)

Installation

Clone the repository:
bashgit clone https://github.com/yourusername/alx_travel_app.git
cd alx_travel_app

Create a virtual environment and activate it:
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
bashpip install -r requirements.txt

Create a .env file by copying the template:
bashcp .env.template .env

Update the .env file with your database credentials and other settings.
Create the MySQL database:
sqlCREATE DATABASE alx_travel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

Run migrations:
bashpython manage.py migrate

Create a superuser:
bashpython manage.py createsuperuser

Start the development server:
bashpython manage.py runserver

In a separate terminal, start Celery worker:
bashcelery -A alx_travel_app worker -l info


API Documentation
API documentation is available at:

Swagger UI: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/

Git Repository
To initialize the Git repository:
bashgit init
git add .
git commit -m "Initial project setup"
