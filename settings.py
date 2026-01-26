import os
from dotenv import load_dotenv

load_dotenv('.env.py')

DB_PASSWORD = os.getenv('PASSWORD')
DB_HOST = os.getenv('HOST')
DB_PORT = os.getenv('PORT')
DB_NAME = os.getenv('NAME')
DB_USER = os.getenv('USER')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        }
    }


INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
