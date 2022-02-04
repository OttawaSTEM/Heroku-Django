"""
For local development "python manage.py runserver"
"""

import os

from django.core.asgi import get_asgi_application
# from django.core.wsgi import get_wsgi_application

if os.environ.get('DJANGO_ENVIRONMENT') == 'Development':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.development')
elif os.environ.get('DJANGO_ENVIRONMENT') == 'Container':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.container')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.virtualmachine')

application = get_asgi_application()
# application = get_wsgi_application()