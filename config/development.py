from config.default import *

<<<<<<< HEAD
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'app.db'))
=======
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
>>>>>>> 3ce3c922b9ba1a78fc37939f54bc7212dd3969a8
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"
