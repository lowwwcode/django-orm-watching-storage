import os
from dotenv import load_dotenv
load_dotenv()

db_engine = os.getenv('DATABASE_ENGINE')
db_host = os.getenv('DATABASE_HOST')
db_port = os.getenv('DATABASE_PORT')
db_name = os.getenv('DATABASE_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASS')

django_secret_key = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'HOST': db_host,
        'PORT': db_port,
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = django_secret_key

DEBUG = False

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
