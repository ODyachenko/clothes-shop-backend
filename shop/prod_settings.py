import environ
import os
import dj_database_url

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('PROD_SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['.vercel.app', '.now.sh', 'localhost']

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

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default']['OPTIONS']['charset'] = 'utf8mb4'
del DATABASES['default']['OPTIONS']['sslmode'] 
DATABASES['default']['OPTIONS']['ssl'] =  {'ca': os.environ.get('MYSQL_ATTR_SSL_CA')}


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')