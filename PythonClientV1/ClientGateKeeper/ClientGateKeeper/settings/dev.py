import os

#DRS Blockchain Address
CONTRACT_ADDRESS = '0xF54a6dE3F1FE973c73BfBb9a5B35D3695Ea277D2'

# DRS Service ID
SERVICE_ID = ''

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
