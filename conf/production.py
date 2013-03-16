# -*- coding: utf-8 -*-

from base import *


CONTACT_EMAIL = "contactus@culination.co"
DEFAULT_FROM_EMAIL = "no-replies@culination.co"

EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_DEBUG = False

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAJNDCQNNOONNJ6VCA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'culination'
AWS_HEADERS = {
    'Expires': 'Tue, 14 Aug 2013 20:00:00 GMT',
    'Cache-Control': 'max-age=8640000',
    }

MEDIA_URL = "http://cookcadmey.s3.amazonaws.com/"

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': None,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'PICKLE_VERSION': 2,
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'culination_prod',
        'USER': "culination_prod",
        'PASSWORD': "epCauftIc8",
        'HOST': '127.0.0.1',
        'PORT': "5432",
    }
}

HTTPS_SUPPORT=True


MIDDLEWARE_CLASSES +=  ("mezzanine.core.middleware.FetchFromCacheMiddleware",)


TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)




####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
