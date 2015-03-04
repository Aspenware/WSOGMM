"""
WSGI config for WSOGMM project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WSOGMM.settings")
application = get_wsgi_application()

try:
    if os.environ['ENVIRONMENT'] is 'Production':
        application = Cling(application)
except KeyError:
    pass