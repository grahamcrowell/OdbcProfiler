"""
Django settings for ProfilesPortal project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6%k_6betb@ucd_*_asgz(f63a#5h%t(b!ebrw*5did$rm-)4a@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'SqlProfiles.apps.SqlprofilesConfig',
    
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

ROOT_URLCONF = 'ProfilesPortal.urls'

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

WSGI_APPLICATION = 'ProfilesPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
   'default': {
       'ENGINE': "sql_server.pyodbc",
       'NAME': "AutoTest",
       'HOST': "STDBDECSUP01",
       'DRIVER':"ODBC Driver 11 for SQL Server",
    #    'USER':'ProfilesPortal',
    #    'PASSWORD':'2and2is5',
   }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'ProfilesPortal',
#         'USER': 'sa',
#         'PASSWORD': '2and2is5',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# # https://github.com/lionheart/django-pyodbc
# DATABASES = {
#    'default': {
#        'ENGINE': "django_pyodbc",
#     #    'USER': "sa",
#     #    'PASSWORD': "2and2is5",
#        'DSN': "ProfilesPortal",
#        'NAME': "ProfilesPortal",
#     #    'OPTIONS': {
#         #    'host_is_server': True
#     #    },
#    }
# }


# # # https://github.com/lionheart/django-pyodbc
# DATABASES = {
#    'default': {
#        'ENGINE': "django_pyodbc",
#        'USER': "",
#        'PASSWORD': "",
#        'NAME': "ProfilesPortal",
#        'HOST': "STDBDECSUP01",
#        'PORT':'1433',
#     #    'OPTIONS': {
#         #    'host_is_server': True
#     #    },
#    }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'sqlserver_ado',
#         'NAME': 'ProfilesPortal',
#         'SERVER': 'STDBDECSUP01',
#         'USER': '',
#         'PASSWORD': '',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)