"""
WSGI config for AWS_3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AWS_3.settings")

os.environ["CELERY_LOADER"] = "django" # may need this

application = get_wsgi_application()