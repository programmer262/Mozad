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

ALLOWED_HOSTS = ['khadioumelmouminine.herokuapp.com','127.0.0.1']

JAZZMIN_SETTINGS = {
  "site_title": "2BAC-PC-F-A-2",
  "site_header": "2BAC-PC-F-A-2",
  "site_logo": "docs/jjj.png",
  "welcome_sign": "Welcome to the 2BAC-PC-F-A-2 .Only for students of khadija oum elmouminine!!!",
  "copyright" : "Developers United Ltd",
  "search_model": "download.classe",
  "user_avatar": None,
  "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url":"https://developers-united.netlify.app", "new_window":True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "download"},
    ],
   "usermenu_links": [
        {"name": "Support", "url": "https://developers-united.netlify.app", "new_window":True},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "download", "download.Etudiant", "download.professor"],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "download.professeur":"fas fa-chalkboard-teacher",
        "download.etudiant":"fas fa-user-graduate",
        "download.emploi":"fas fa-hourglass-half",
        "download.classe":"far fa-eye",
        "download.live_ended":"far fa-eye-slash",
        "download.cour":"fas fa-book-reader",
        "download.exercice":"fas fa-book",
        "download.corrigé":"fas fa-book",
        "download.matiére":"fas fa-school",
        "download.heure":"fas fa-hourglass",
        "download.présence":"fas fa-graduation-cap"

    },
    "related_modal_active": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs",},
    "language_chooser": False,

}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'download',

]

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
        'DIRS': ['/download/Templates/Files'],
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


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd9t4mvafduhv9p',
        'USER': 'bkkhzfwphfesaa',
        'PASSWORD': '7afad86151ecdb48fc1003fb66365fac91a2e0b745b6dac95fc2a6320902d24c',
        'HOST': 'ec2-34-239-241-25.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}


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

TEMPLATE_URL = 'download/Templates/'
TEMPLATES_DIRS = [
    os.path.join(BASE_DIR, 'download/Templates/')
]
STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')
STATIC_URL = STATIC_HOST + '/static/'
STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/docs/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/docs')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
