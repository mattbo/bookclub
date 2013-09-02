# Django settings for bookclub project.
from bookclub.settings import *

DEBUG = False

ADMINS = (
  ('Matt Bosworth', 'matt@codetastic.com'),
)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.codetastic.com', ]

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/home7/codetast/public_html/bookclub/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/bookclub/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's3x2zr2@od%*u-2u8^5ev!!rqi*=bc8ff)$a-#94#7zv$#s+50'

#LOGIN_URL='/bookclub/accounts/login'
LOGIN_URL='django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = '/bookclub/club'
FORCE_SCRIPT_NAME = '/bookclub'
