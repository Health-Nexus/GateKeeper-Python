import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DRS_SECRET_KEY',None)
if not SECRET_KEY:
    raise ValueError('You must have "SECRET_KEY" variable')


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = bool( os.environ.get('DRS_DEBUG', False) )

#DRS Blockchain Address
CONTRACT_ADDRESS = os.environ.get('DRS_CONTRACT_ADDRESS',None)
if not CONTRACT_ADDRESS:
    raise ValueError('You must have "CONTRACT_ADDRESS" variable')

# DRS Service ID
SERVICE_ID = os.environ.get('DRS_SERVICE_ID',None)
if not SERVICE_ID:
    raise ValueError('You must have "SERVICE_ID" variable')

# Database credentials
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'drsdb',
        'USER': 'drs',
        'PASSWORD': 'abcd12345',
        'HOST': 'localhost',
        'PORT': '',
    }
}