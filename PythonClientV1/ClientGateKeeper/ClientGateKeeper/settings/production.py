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

# DRS Service ID - possibly get this from database
SERVICE_IDS = ['0xa2e73b1bae8003a768b7876e021838e060e36d5bf80bf425652ef9381fb2b7e1','0xa2e73b1bae8003a768b7876e021838e060e36d5bf80bf425652ef9381fb2b7e1']
if not SERVICE_IDS:
    raise ValueError('You must have "SERVICE_IDS" variable')

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