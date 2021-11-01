import os

COUNTRY_CURRENCY_PLN = "PLN"
NBP_API_URL = "http://api.nbp.pl/api/exchangerates/rates/a"


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{ os.environ.get('PSQL_USER_NAME')}:{os.environ.get('PSQL_PASS')}@localhost/{os.environ.get('PSQL_DB_NAME')}"

class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
