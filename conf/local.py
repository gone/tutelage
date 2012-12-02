from base import *

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'local.db'
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'tutelage'
    }
}


TRANSLOADIT_URL = 'http://api2.transloadit.com/assemblies'
TRANSLOADIT_SECRET = '1b13c165c4895ab9ad63d2fc7c14530d92b9ec75'
TRANSLOADIT_AUTH = 'f0a96080595246828f687bb61ece3ae2'
TRANSLOADIT_HTML5_VIDEO_TEMPLATE = 'a39b0b5afdb343b9a2b3adb0994396fc'
TRANSLOADIT_DATAFIELD = 'transloadit'

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
