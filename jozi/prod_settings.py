from base_settings import *

ADMINS = (
    ('Adrian Hughes', 'adrianjbhughes@gmail.com'),
    ('Alex Hughes', 'alex@customsoftuk.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'jozi',
        'USER': 'jozi_admin',
        'PASSWORD': 'fr3dalex',
        'HOST': 'localhost',
        'PORT': '',
	}
}
TIME_ZONE = 'Africa/Johannesburg'
