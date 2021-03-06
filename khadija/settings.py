"""
Django settings for khadija project.
Generated by 'django-admin startproject' using Django 3.1.1.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gso5fc6^ps3wkk2re^ann3r2v!psc*_-uc%u-f2rd^-rv(#24_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['demoprogrammer262.herokuapp.com','127.0.0.1']
JAZZMIN_SETTINGS = {
  "site_title": "Demo",
  "site_header": "Demo",
  "site_logo": "docs/jjj.png",
  "welcome_sign": "Welcome to the Demo of achraf chahin!!!",
  "copyright" : "Developers United Ltd",
  "search_model": "auth.user",
  "user_avatar": None,
  "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "View Site", "url": "https://khadioumelmouminine.herokuapp.com/", "new_window":True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "download"},
    ],
   "usermenu_links": [
        {"name": "View Site", "url": "https://demoprogrammer262.herokuapp.com/", "new_window":True},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,
    "hide_apps": [],
    "order_with_respect_to": ["auth"],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "download.cour" : "fas fa-book-reader",
        "download.exercice" : "fas fa-dumbbell",
        "download.corrigé" : "fas fa-times",
        "download.classe" : "fas fa-eye",
        "download.live_ended" : "fas fa-eye-slash",
        "download.etudiant" : "fas fa-graduation-cap",
        "download.professor" : "fas fa-chalkboard-teacher",
        "download.matiére" : "fas fa-brain",
    },
    "related_modal_active": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs","store.product": "vertical_tabs",},
    "language_chooser": False,

}


INSTALLED_APPS = [ 
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'download',]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'khadija.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'khadija.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd6s3sb1u74p7sg',
        'USER': 'qzxersyidcnzxn',
        'PASSWORD': 'fc77be2d4965e9e731749fcb0e6634fbcab3fc300a5b9ee43dfb917bace083b7',
        'HOST': 'ec2-184-73-249-9.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

# Cloudinary settings using python code. Run before pycloudinary is used.


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')
STATIC_URL = STATIC_HOST + '/static/'
STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/docs/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/docs')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
