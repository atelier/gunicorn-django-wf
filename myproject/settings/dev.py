from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/New_York'

SITE_ID = 1

MEDIA_ROOT = '' # Example: "/home/me/mysite/media/"
MEDIA_URL = 'http://localhost:8000/common/'
ADMIN_MEDIA_PREFIX = '/admin/media/'

TEMPLATE_DIRS = () # Example: ('/home/me/mysite/templates')