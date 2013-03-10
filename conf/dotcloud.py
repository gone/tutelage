# -*- coding: utf-8 -*-

from base import *


CONTACT_EMAIL = "contactus@wellganic.com"
DEFAULT_FROM_EMAIL = "wellganic@wellganic.com"

EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_DEBUG = False

DEBUG = True

import json
with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

try:
  mod = __import__("settings." + env["DOTCLOUD_PROJECT"], globals(), locals(), fromlist="*")
  for attr in dir(mod):
    if attr.startswith("__"):
      continue
    globals()[attr] = getattr(mod, attr)
except ImportError:
  pass


# from S3 import CallingFormat
# AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

# AWS_STATIC_STORAGE_BUCKET_NAME = 'static.tutelage.com'
# AWS_STATIC_ACCESS_KEY_ID = ''
# AWS_STATIC_SECRET_ACCESS_KEY = ''
# AWS_HEADERS = {
#         'Cache-Control': "max-age:5, public"
#     }

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# EMAIL_BACKEND = "django_ses.SESBackend"
# AWS_SES_ACCESS_KEY_ID = ''
# AWS_SES_SECRET_ACCESS_KEY = ''

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAJNDCQNNOONNJ6VCA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'culination'
AWS_HEADERS = {
    'Expires': 'Tue, 14 Aug 2013 20:00:00 GMT',
    'Cache-Control': 'max-age=8640000',
    }

MEDIA_URL = "http://cookcadmey.s3.amazonaws.com/"
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATIC_URL = "http://cookcadmey.s3.amazonaws.com/"





#INSTALLED_APPS += ('redis_status',)

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': env['DOTCLOUD_CACHE_REDIS_HOST'] + ":" + env['DOTCLOUD_CACHE_REDIS_PORT'],
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': env['DOTCLOUD_CACHE_REDIS_PASSWORD'],
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'PICKLE_VERSION': 2,
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wellganic',
        'USER': env['DOTCLOUD_DATA_SQL_LOGIN'],
        'PASSWORD': env['DOTCLOUD_DATA_SQL_PASSWORD'],
        'HOST': env['DOTCLOUD_DATA_SQL_HOST'],
        'PORT': int(env['DOTCLOUD_DATA_SQL_PORT']),
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
