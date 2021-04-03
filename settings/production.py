from . import *

SECRET_KEY = 'jR$x0b]W]?vn<FMN!9K}7p$hE}|'
DEBUG = False
ALLOWED_HOSTS = ['159.89.8.181']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME': 'purbeurre', # le nom de notre base de données créée précédemment
        'USER': 'rol', # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': 'mdp123mdp',
        'HOST': '',
        'PORT': '5432',
    }
}

import logging
import sentry_sdk
from sentry_sdk import set_level
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
sentry_logging = LoggingIntegration(
    level=logging.INFO,        
    event_level=logging.INFO
)
set_level("info")

sentry_sdk.init(
    dsn="https://04ef3937c89c464c9447bdec16877d53@o559490.ingest.sentry.io/5695055",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


