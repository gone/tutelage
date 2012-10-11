DEBUG = True

#EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAJNDCQNNOONNJ6VCA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'cookcadmey'
AWS_HEADERS = {
    'Expires': 'Tue, 14 Aug 2013 20:00:00 GMT',
    'Cache-Control': 'max-age=8640000',
    }

MEDIA_URL = "http://cookcadmey.s3.amazonaws.com/"
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATIC_URL = "http://cookcadmey.s3.amazonaws.com/"
