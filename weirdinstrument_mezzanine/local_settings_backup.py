from __future__ import unicode_literals

SECRET_KEY = "fagsw63a#f0fz*9ab0uff^idfgw67+r&dx06ul#ildj604&_ou"
NEVERCACHE_KEY = "d8jhfjzq#@(#+yzhc4#cs6al(u%*lvw4vtq^36dp4psbub9dj@"
ALLOWED_HOSTS = ['www.kissabc.xyz', 'www.liufei-piano-studio.com', 'www.weirdinstrument.com']
#
# DATABASES = {
#     "default": {
#         # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
#         # "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         # DB name or path to database file if using sqlite3.
#         "NAME": "weirdinstrument_mezzanine",
#         # Not used with sqlite3.
#         "USER": "weirdinstrument_mezzanine",
#         # Not used with sqlite3.
#         "PASSWORD": "liufei921",
#         # Set to empty string for localhost. Not used with sqlite3.
#         "HOST": "127.0.0.1",
#         # Set to empty string for default. Not used with sqlite3.
#         "PORT": "",
#     }
# }

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        # "ENGINE": "django.db.backends.postgresql_psycopg2",
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "weirdinstrument_mezzanine.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}



SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "weirdinstrument_mezzanine"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"


