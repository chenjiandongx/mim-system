import os

here = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = '#+^aOjdlPHFD09)&*2P3JR-0CFE)&H12EAa;OPFG=0'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + os.path.join(here, 'data-dev.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
