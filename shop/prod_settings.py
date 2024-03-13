import environ
import os
import dj_database_url

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['.vercel.app', '.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(
        default=env('HEROKU_POSTGRESQL_PUCE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}
