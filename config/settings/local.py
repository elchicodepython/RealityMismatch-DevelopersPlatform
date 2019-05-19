from .base import *


DEBUG = True

SECRET_KEY = 'q8t+o@xj#$jsnjsrz=$wgb%tobzpkvp!$aw+l)wua&%c9=g3wr'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'realitymismatch_developers',
        'HOST': '127.0.0.1',
        'USER': 'developer',
        'PASSWORD': 'dtYtxjDxugBIsn2toHig'
    }
}
