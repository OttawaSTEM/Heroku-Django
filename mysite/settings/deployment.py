from .base import *

DEBUG = False           # Must run "python manage.py collect static", otherwise cause Server Error (500)
CSRF_TRUSTED_ORIGINS = ['ottawastem-django.herokuapp.com']      # When DEBUG=False in Deployment