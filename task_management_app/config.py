# Configuration settings
# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # SQLite database file
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key_here'  # Replace with a secure key