"""
Django settings for projeto_vyf project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5!$8!^j=flxx-sq2_&*rz2zi&m75a5ib$l7vluc+0%82mc4_o0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TEMPLATE_DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli', # para incluir grappelli
    'filebrowser',
    'artigos',
    # 'noticias',
    'polls',
    'categorias',
    'bio',
    'eventos',
    'testes',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.syndication', # para adicionar o RSS
    'django.contrib.sites',
    'django.contrib.comments', # para comentarios
    'debug_toolbar',
    'django.contrib.admindocs',
    # 'django_select2', # para usar o Select2, nao esquecer o collectstatic
    'easy_select2', # para usar os campos do Select2 no admin
    'django.contrib.redirects', # para redirecionamento de url

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware', # para redirecionar url
)

ROOT_URLCONF = 'projeto_vyf.urls'

WSGI_APPLICATION = 'projeto_vyf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# configuracoes para select2:
# AUTO_RENDER_SELECT2_STATICS = True # True para o select2 incluir os <script> <link> automaticamente
# SELECT2_MEMCACHE_HOST = None
# SELECT2_MEMCACHE_PORT = None
# SELECT2_MEMCACHE_TTL = 900


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

SITE_ID = 2

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = 'http://localhost:8080/'

FILEBROWSER_DIRECTORY = ''
# FILEBROWSER_DIRECTORY = getattr(settings, "FILEBROWSER_DIRECTORY", 'uploads/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "_static")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "project_static"),
)



# para a home index.html colocado a pasta da raiz template para chamar a home sem procurar nas pasts do app
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

