from .base import *
from ..utils import get_env_variable


DEBUG = False

SECRET_KEY = get_env_variable('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DB_NAME'),
        'HOST': get_env_variable('DB_HOST')
    }
}
