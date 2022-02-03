"""
For local development "python manage.py runserver"
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.development')

application = get_wsgi_application()