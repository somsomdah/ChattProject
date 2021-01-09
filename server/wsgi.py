"""
WSGI server for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
#from whitenoise.django import DjangoWhiteNoise



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings.prod')

application = get_wsgi_application()
application = WhiteNoise(application,root='/home/ubuntu/srv/Chatt-project-backend/staticfiles')
#application = DjangoWhiteNoise(application)




