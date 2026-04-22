from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent  # points to outer student_analytics/

SECRET_KEY = 'django-insecure-student-analytics-key-2024'
DEBUG = False
ALLOWED_HOSTS = ['FARAAZ.pythonanywhere.com']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'student_analytics.urls'   # ← inner package name

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.request',
        ],
    },
}]

WSGI_APPLICATION = 'student_analytics.wsgi.application'

# sqlite3 database engine and database file located in BASE_DIR 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # tells Django WHICH database engine to use
        'NAME': BASE_DIR / 'db.sqlite3', # tells Django WHERE the database file is
    }
}

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_ENGINE = 'django.contrib.sessions.backends.file' 
SESSION_FILE_PATH = BASE_DIR / 'sessions'
os.makedirs(SESSION_FILE_PATH, exist_ok=True)

STATIC_ROOT = BASE_DIR / 'staticfiles'