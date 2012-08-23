
DEBUG = False
import json
with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)


if env["DOTCLOUD_PROJECT"] != "zombies":
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
    DEBUG = True
else:
    EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tutelage',
        'USER': env['DOTCLOUD_DATA_SQL_LOGIN'],
        'PASSWORD': env['DOTCLOUD_DATA_SQL_PASSWORD'],
        'HOST': env['DOTCLOUD_DATA_SQL_HOST'],
        'PORT': int(env['DOTCLOUD_DATA_SQL_PORT']),
    }
}
