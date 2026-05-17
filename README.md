# CIT389 Django Elastic Beanstalk App

This repository contains a simple Django web application created for CIT389 coursework. The project demonstrates how to build a basic Python/Django web app and prepare it for deployment on AWS Elastic Beanstalk.

The application displays a simple homepage message:

```text
Hello World!
Welcome to Elastic Beanstalk Django App!
```

## Project Purpose

The purpose of this project is to practice the full workflow of creating, configuring, and deploying a Django application using AWS services.

This project helps demonstrate:

- Basic Django project structure
- URL routing in Django
- Creating a simple Django view
- Using WSGI for deployment
- Preparing a Django app for AWS Elastic Beanstalk
- Managing Python dependencies with `requirements.txt`
- Using a build configuration file for deployment packaging

## Technologies Used

- Python
- Django 5.0.2
- Gunicorn
- AWS Elastic Beanstalk
- AWS CodeBuild / BuildSpec
- GitHub

## Repository Structure

```text
cit389App_repo/
│
├── .ebextensions/
│   └── django.config
│
├── mysite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── application.py
├── buildspec.yml
├── manage.py
├── requirements.txt
└── README.md
```

## File Guide

### `application.py`

This file exposes the Django WSGI application for AWS Elastic Beanstalk.

```python
from mysite.wsgi import application
```

Elastic Beanstalk uses this file to locate and run the Django application.

### `mysite/settings.py`

This file contains the main Django project settings, including:

- Project base directory
- Secret key
- Debug mode
- Allowed hosts
- Installed apps
- Middleware
- Static file settings
- WSGI application path

Important settings used in this project include:

```python
DEBUG = True
ALLOWED_HOSTS = ['*']
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### `mysite/views.py`

This file contains the view function for the homepage.

The homepage returns a simple HTTP response:

```text
Hello World!
Welcome to Elastic Beanstalk Django App!
```

### `mysite/urls.py`

This file maps the root URL of the website to the homepage view.

```python
urlpatterns = [
    path('', views.home),
]
```

When a user visits the root URL `/`, Django calls the `home` view.

### `mysite/wsgi.py`

This file creates the WSGI application used by the web server.

WSGI is required for deploying Django applications to production environments such as AWS Elastic Beanstalk.

### `.ebextensions/django.config`

This file tells AWS Elastic Beanstalk where to find the WSGI application.

The WSGI path is configured as:

```text
application:application
```

This means Elastic Beanstalk should use the `application` object inside the root-level `application.py` file.

### `requirements.txt`

This file lists the Python dependencies required to run the project.

Current dependencies:

```text
Django==5.0.2
gunicorn
```

Install these dependencies using:

```bash
pip install -r requirements.txt
```

### `buildspec.yml`

This file defines the build process for AWS CodeBuild or deployment packaging.

The build process:

1. Uses Python 3.11
2. Upgrades pip
3. Installs dependencies from `requirements.txt`
4. Packages the full project directory as the deployment artifact

## How to Run the Project Locally

Follow these steps to run the project on your local machine.

### Step 1: Clone the Repository

```bash
git clone https://github.com/iamwaqarjaved/cit389App_repo.git
cd cit389App_repo
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Run the Django Development Server

```bash
python manage.py runserver
```

### Step 6: Open the App in a Browser

Visit:

```text
http://127.0.0.1:8000/
```

You should see:

```text
Hello World!
Welcome to Elastic Beanstalk Django App!
```

## AWS Elastic Beanstalk Deployment Guide

This project is already prepared for AWS Elastic Beanstalk deployment.

### Step 1: Confirm Required Files Exist

Make sure the following files are included in the repository:

```text
application.py
requirements.txt
.ebextensions/django.config
mysite/wsgi.py
mysite/settings.py
```

### Step 2: Confirm the WSGI Path

The Elastic Beanstalk configuration should point to:

```text
application:application
```

This means:

- The first `application` refers to `application.py`
- The second `application` refers to the WSGI application object

### Step 3: Deploy to Elastic Beanstalk

You can deploy the project using the AWS Elastic Beanstalk Console or AWS CLI.

General deployment flow:

1. Create an Elastic Beanstalk application
2. Choose Python as the platform
3. Upload the project source bundle
4. Allow Elastic Beanstalk to install dependencies
5. Launch the environment
6. Open the provided Elastic Beanstalk URL

## Development Workflow

A basic development workflow for this project:

```bash
git clone https://github.com/iamwaqarjaved/cit389App_repo.git
cd cit389App_repo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

After making changes:

```bash
git add .
git commit -m "Update Django application"
git push origin main
```

## Security Notes

The current project uses development-friendly settings:

```python
DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'replace-me'
```

Before using this project in a real production environment, update these settings.

Recommended production changes:

- Set `DEBUG = False`
- Replace the default `SECRET_KEY`
- Store sensitive values in environment variables
- Restrict `ALLOWED_HOSTS` to trusted domains
- Configure a production database if needed
- Run `python manage.py collectstatic` for static files

## Common Commands

Run the development server:

```bash
python manage.py runserver
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a new Django app:

```bash
python manage.py startapp appname
```

Collect static files:

```bash
python manage.py collectstatic
```

Check for Django issues:

```bash
python manage.py check
```

## Troubleshooting

### Issue: Dependencies Not Installing

Try upgrading pip first:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: App Does Not Start on Elastic Beanstalk

Check that `.ebextensions/django.config` has the correct WSGI path:

```text
application:application
```

Also confirm that `application.py` exists in the project root.

### Issue: Static Files Not Loading

Run:

```bash
python manage.py collectstatic
```

Also confirm that `STATIC_URL` and `STATIC_ROOT` are configured in `settings.py`.

### Issue: Local Server Not Running

Make sure the virtual environment is activated and dependencies are installed:

```bash
pip install -r requirements.txt
python manage.py runserver
```

## Important Formatting Note

Some files in the repository may need to be checked for proper line breaks and indentation. For better readability and to avoid syntax issues, Python and YAML files should be formatted correctly.

Files that should be checked:

```text
manage.py
application.py
buildspec.yml
mysite/settings.py
mysite/urls.py
mysite/views.py
mysite/wsgi.py
mysite/asgi.py
.ebextensions/django.config
```

## Future Improvements

Possible improvements for this project:

- Add HTML templates
- Add CSS styling
- Add a database model
- Add Django admin support
- Add environment variable support
- Add unit tests
- Add a production-ready settings file
- Configure custom domain support
- Add CI/CD deployment automation

## Author

Waqar Javed

GitHub: [iamwaqarjaved](https://github.com/iamwaqarjaved)

## License

This project is created for academic and learning purposes.
