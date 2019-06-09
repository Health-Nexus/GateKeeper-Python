import os

#DRS Blockchain Address
CONTRACT_ADDRESS = '0xF54a6dE3F1FE973c73BfBb9a5B35D3695Ea277D2'

# DRS Service ID
SERVICE_IDS = ['0x9426e04fe757749698e850c413f730c3970dc88e0d73661c4acc01f7f2d0de74','F54a6dE3F1FE973c73BfBb9a5B35D3695Ea277D2','F54a6dE3F1FE973c73BfBb9a5B35D3695Ea277D2']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'phusedb',
        'USER': 'drs',
        'PASSWORD': 'abcd12345',
        'HOST': 'localhost',
        'PORT': '',
    }
}
