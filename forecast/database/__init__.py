from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from .models import User, Forecast
    db.drop_all()
    db.create_all()
