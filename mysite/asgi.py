"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

if os.environ.get('DJANGO_ENVIRONMENT') == 'Development':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skeleton.settings.development')
elif os.environ.get('DJANGO_ENVIRONMENT') == 'Deployment':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skeleton.settings.deployment')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skeleton.settings.production')

from django.core.asgi import get_asgi_application
application = get_asgi_application()

# Wrap werkzeug debugger if DEBUG is on
from django.conf import settings
if settings.DEBUG:
    try:
        import django.views.debug
        import six
        from werkzeug.debug import DebuggedApplication

        def null_technical_500_response(request, exc_type, exc_value, tb):
            six.reraise(exc_type, exc_value, tb)

        django.views.debug.technical_500_response = null_technical_500_response
        application = DebuggedApplication(application, evalex=True,
                                          # Turning off pin security as DEBUG is True
                                          pin_security=False)
    except ImportError:
        pass
