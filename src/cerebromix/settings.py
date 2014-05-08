# coding: utf-8

"""
Django settings for cerebromix project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from django.conf import global_settings
from decouple import config
from dj_database_url import parse as db_url
from unipath import Path
from decimal import Decimal

BASE_DIR = Path(__file__).parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '.herokuapp.com']

# Django debug toolbar
INTERNAL_IPS = ('127.0.0.1')

# Application definition

SHARED_APPS = (
    'cerebromix.tenant_schemas',  # mandatory
    # you must list the app where your tenant model resides in
    'cerebromix.core',
    'cerebromix.website',
    'cerebromix.customers',
    'cerebromix.plans',

    # You will need add grappelli first that admin
    # 'grappelli.dashboard',  CONFIGURAR DASHBOARDS
    # 'grappelli',

    # 'admin_tools',
    # 'admin_tools.theming',
    # 'admin_tools.menu',
    # 'admin_tools.dashboard',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.admin',
    # 'django.contrib.flatpages',
    'rest_framework',
    'south',
    'debug_toolbar',
    'ordered_model',
    # 'django_generic_flatblocks',
)

TENANT_APPS = (
    # The following Django contrib apps must be in TENANT_APPS
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # your tenant-specific apps
    'rest_framework',
    'south',
)

INSTALLED_APPS = SHARED_APPS + TENANT_APPS + ('cerebromix.tenant_schemas',)

TENANT_MODEL = "customers.Client"  # app.Model

SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2',
}

MIDDLEWARE_CLASSES = (
    'cerebromix.tenant_schemas.middleware.TenantMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #     'django.middleware.http.ConditionalGetMiddleware',
    #     'django.middleware.gzip.GZipMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'cerebromix.plans.context_processors.account_status',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

ROOT_URLCONF = 'cerebromix.urls_tenants'

PUBLIC_SCHEMA_URLCONF = 'cerebromix.urls_public'

WSGI_APPLICATION = 'cerebromix.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='postgres://postgres:root@localhost/cerebromix',
        cast=db_url),
}

#DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
DATABASES['default']['ENGINE'] = 'cerebromix.tenant_schemas.postgresql_backend'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/_/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE__ = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'

# Usar o South para preparar o banco nos testes?
# True: Sim. (default)
# False: Não! Use o Syncdb
SOUTH_TESTS_MIGRATE = False

# Grappelli Config

# GRAPPELLI_ADMIN_TITLE = 'Cerebro Mix Admin'

# GRAPPELLI_SWITCH_USER = True

SITE_ID = 1

# para utilizar a função get_profile()
#AUTH_PROFILE_MODULE = 'cerebromix.customers.models.UserProfile'

ISSUER_DATA = {
    "issuer_name": "My Company Ltd",
    "issuer_street": "48th Suny street",
    "issuer_zipcode": "111-456",
    "issuer_city": "Django City",
    "issuer_country": "PL",
    "issuer_tax_number": "PL123456789",
}

TAX = Decimal('23.0')
TAXATION_POLICY = 'cerebromix.plans.taxation.eu.EUTaxationPolicy'
TAX_COUNTRY = 'PL'

CURRENCY = 'EUR'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# LOGIN_REDIRECT_URL = '/foo/list/'