from .base import *

DEBUG = False           # Must run "python manage.py collect static", otherwise cause Server Error (500)
CSRF_TRUSTED_ORIGINS = eval(env('ALLOWED_HOSTS'))      # When DEBUG=False in Deployment