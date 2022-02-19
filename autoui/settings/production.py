DEBUG = False
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'autoui_project',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

try:
    from .local import *
except:
    pass
'''
use it, when run project in development 
python manage.py runserver --settings=autoui.settings.dev

'''