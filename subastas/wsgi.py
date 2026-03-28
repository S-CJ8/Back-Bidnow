"""
Alias WSGI para despliegues que usan `gunicorn subastas.wsgi:application`
(Render puede tener ese Start Command aunque el proyecto use `config.settings`).
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
