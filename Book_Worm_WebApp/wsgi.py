"""
WSGI config for Book_Worm_WebApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Book_Worm_WebApp.settings')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
# import django
#
# django.setup()
application = get_wsgi_application()
