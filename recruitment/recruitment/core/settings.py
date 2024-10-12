"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from configparser import RawConfigParser
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
JSON_PATH = BASE_DIR.joinpath('json')
CONF_PATH = BASE_DIR.joinpath('conf')

CONFIG = RawConfigParser()
CONFIG.read(CONF_PATH.joinpath('local.conf'), encoding='utf-8')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.get(section='main', option='SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = CONFIG.getboolean(section='main', option='DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
]

for app in ('main', 'recruits', 'sith'):
    INSTALLED_APPS.append(f'{app}_app.apps.{app.capitalize()}AppConfig')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': CONFIG.get(section='db', option='DATABASE_ENGINE'),
        'NAME': BASE_DIR.joinpath(
            CONFIG.get(section='db', option='DATABASE_NAME'),
        ),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'main_app.CustomUser'

password_validation = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f'{password_validation}.UserAttributeSimilarityValidator',
    },
    {
        'NAME': f'{password_validation}.MinimumLengthValidator',
    },
    {
        'NAME': f'{password_validation}.CommonPasswordValidator',
    },
    {
        'NAME': f'{password_validation}.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.joinpath(
        CONFIG.get(section='main', option='STATICFILES_DIRS'),
    ),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath(
    CONFIG.get(section='main', option='MEDIA_ROOT'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# to record log messages to files
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/email-messages/'

section_name = 'superuser'
SUPERUSER_DATA = {
    'username': CONFIG.get(section=section_name, option='username'),
    'email': CONFIG.get(section=section_name, option='email'),
    'password': CONFIG.get(section=section_name, option='password'),
    'age': CONFIG.getint(section=section_name, option='age'),
    'first_name': CONFIG.get(section=section_name, option='first_name'),
    'last_name': CONFIG.get(section=section_name, option='last_name'),
    'role': CONFIG.get(section=section_name, option='role'),
    'planet': CONFIG.get(section=section_name, option='planet'),
    'is_shadow_hand': CONFIG.getboolean(
        section=section_name,
        option='is_shadow_hand',
    ),
}
