from .base import *
import os
ALLOWED_HOSTS = ["*"]
CSRF_COOKIE_SECURE = False
DEBUG = os.getenv("DEBUG",False)

SECRET_KEY = os.getenv("SECRET_KEY", "secret!")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME", "postgres"),
        'USER': os.getenv("DB_USER", "postgres"),
        'PASSWORD': os.getenv("DB_PASSWORD", "password"),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", '5432'),
    }
}

GOOGLE_ANALYTICS_PROPERTY_ID = os.getenv('GA_TOKEN','UA-XXXXXXX-X')
BASE_URL = os.getenv("BASE_URL",'http://example.com')
WAGTAIL_SITE_NAME = os.getenv("WAGTAIL_SITE_NAME" ,"web")

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME','####')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID','####')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY','####')
AWS_S3_CUSTOM_DOMAIN = 's3.us-east-2.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

try:
    from .local import *
except ImportError:
    pass
