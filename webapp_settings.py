"""
Django settings for testsite project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).parent.resolve()
PROJECT_DIR = Path(__file__).parent.resolve()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)c_fz7uigyit*w6-#107v&8o6(4@sm%y^wl9=zzw3x(5%e$ml2'

from os import getenv
from dotenv import load_dotenv

# SECURITY WARNING: don't run with debug turned on in production!
load_dotenv()
DEBUG:bool = getenv('DEBUG', 'False').lower() == 'true'
DEBUG_FRONTEND:bool = getenv('DEBUG_FRONTEND', 'False').lower() == 'true'
ALLOWED_HOSTS = [getenv('ALLOWED_HOSTS', '*')]

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'create_react_app',
    'channels'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webapp_urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path.joinpath(PROJECT_DIR, 'templates')],
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

# WSGI_APPLICATION = 'webapp.wsgi.application'
ASGI_APPLICATION = "webapp_asgi.application"
CHANNEL_LAYERS = { "default": {"BACKEND": "channels.layers.InMemoryChannelLayer" }}
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:' #BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Create React App

WEBPACK_DEV_SERVER_URL = "http://localhost:3000/"
REACT_BUILD_DIRECTORY = Path.joinpath(PROJECT_DIR, 'build')

CREATE_REACT_APP = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': REACT_BUILD_DIRECTORY,  
        'FRONT_END_SERVER': WEBPACK_DEV_SERVER_URL,
        'is_dev': DEBUG_FRONTEND,
    }
}

WDS_SOCKET_HOST = "localhost:3000"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = Path.joinpath(PROJECT_DIR, 'static')

STATICFILES_DIRS = [
    Path.joinpath(REACT_BUILD_DIRECTORY, 'static'),
    Path.joinpath(PROJECT_DIR, 'public')
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
