class Config:
    Debug = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////home/akula/Документы/Communuity_pulse_app/database_1.db'

class DeveloperConfig(Config):
    DEBUG = True

class Testing(Config):
    DEBUG = True
    TESTING = True

