"""
Django settings for csp project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, django
import dj_database_url
from distutils.version import StrictVersion
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from spirit.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v1*ah#)@vyov!7c@n&c2^-*=8d)-d!u9@#c4o*@k=1(1!jul6&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
APPEND_SLASH = True

# ALLOWED_HOSTS = [*]

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',),
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        #'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    #'PAGE_SIZE': 100
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
}

OAUTH2_PROVIDER_APPLICATION_MODEL = 'oauth2_provider.Application'
MIGRATION_MODULES = {
    'oauth2_provider': 'crowdsourcing.migrations.oauth2_provider',
}

INSTALLED_APPS += (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'compressor',
    'rest_framework',
    'oauth2_provider',
    'crowdsourcing',
    'autofixture',

)

MIDDLEWARE_CLASSES += (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'csp.urls'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'static/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

WSGI_APPLICATION = 'csp.wsgi.application'



DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
COMPRESS_ROOT = '/compress'
#Python 2
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'static/templates'),
)

# Email
EMAIL_HOST = 'localhost'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_ENABLED = True
EMAIL_SENDER = 'daemo@cs.stanford.edu'
EMAIL_SENDER_DEV = 'crowdsourcing.platform.demo@gmail.com'
EMAIL_SENDER_PASSWORD_DEV = 'crowdsourcing.demo.2015'
SENDGRID_API_KEY = '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'

# Others
REGISTRATION_ALLOWED = False
PASSWORD_RESET_ALLOWED = True

LOGIN_URL = '/login'
#SESSION_ENGINE = 'redis_sessions.session'

# Security
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
PYTHON_VERSION = 2
try:
    from local_settings import *
except Exception as e:
    pass


GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

if StrictVersion(django.get_version())<'1.8':
    FIXTURE_DIRS = (
        os.path.join(BASE_DIR, 'fixtures')
    )

USERNAME_MAX_LENGTH = 30


# Google Drive
GOOGLE_DRIVE_CLIENT_ID = '960606345011-3bn8sje38i9c0uo8p87ln6tfb2dhco9v.apps.googleusercontent.com'
GOOGLE_DRIVE_CLIENT_SECRET = 'v-gWQKOmuAhTmbJ5REwH-V_1'
GOOGLE_DRIVE_OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
GOOGLE_DRIVE_REDIRECT_URI = 'http://localhost:8000/api/google-auth-finish'

# Dropbox
DROPBOX_APP_KEY = '__KEY__'
DROPBOX_APP_SECRET = '__SECRET__'
DROPBOX_REDIRECT_URI = 'http://localhost:8000/api/dropbox-auth-finish'
