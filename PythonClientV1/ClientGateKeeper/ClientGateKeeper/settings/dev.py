import os

#DRS Blockchain Address
CONTRACT_ADDRESS = '0x1ba6cea196f186e6ee2d8ac46308e6d18018e910'

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
