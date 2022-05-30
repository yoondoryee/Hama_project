from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x91\x90\xe5,\xe7\xe1\xe1\xaf\xcc\xf5MZ<\x8dN\xc6'
