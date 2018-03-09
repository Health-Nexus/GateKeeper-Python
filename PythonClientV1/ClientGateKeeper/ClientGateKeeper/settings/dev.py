import os

#DRS Blockchain Address
CONTRACT_ADDRESS = '0x1ba6cea196f186e6ee2d8ac46308e6d18018e910'

# DRS Service ID
SERVICE_ID = '0x5c07c33f7fdc925a2a9154b4391503aa6088c651f1757e09fcb7006399582e4d'

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