import secrets
import urllib.parse as parse

class Config:
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:labinfo@localhost:3306/instituicao"