import environ
import os

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('PROD_SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': env('DB_NAME'),  
        'USER': env('DB_USER'),  
        'PASSWORD': env('DB_PASSWORD'),  
        'HOST': env('DB_HOST'),  
        'PORT': env('DB_PORT'),  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')