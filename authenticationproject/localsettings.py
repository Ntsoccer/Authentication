import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4nh%ra3__wds+%+iu4it#tc&e%=nq$t5qe4w&)*-)agv7er$m5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '470937454052-iifs4kqr895ptjvbg7cac258ak42aiku.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'V4HHvXuFo7zFAqYnzIwOYUsH'

SOCIAL_AUTH_FACEBOOK_KEY = '2375000696129949'
SOCIAL_AUTH_FACEBOOK_SECRET = '39215f0790ccf19f0be4b368e11189ee'
