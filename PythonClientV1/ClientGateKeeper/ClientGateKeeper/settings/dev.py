import os

#DRS Blockchain Address
CONTRACT_ADDRESS = '0x2c104bb9E7098Ccc5a537caF2daE52caC4E4e5B5'

# DRS Service ID
SERVICE_ID = '0x9426e04fe757749698e850c413f730c3970dc88e0d73661c4acc01f7f2d0de74'

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
