from sqlalchemy.orm.exc import NoResultFound
from forecast.database.models import User, Forecast, Period, Days
from forecast.database import db


def add_user(data):
    name = data.get('name')

    try:
        user = User.query.filter(User.name == name).one()
    except NoResultFound:
        user = User(name)
        db.session.add(user)
        db.session.commit()

    # Foreign Key
    if data.get('forecast'):
        for fc in data.get('forecast'):
            add_forecast(fc, user.id)

    return user


def add_forecast(data, user_id):
    address = data.get('address')
    notification = data.get('notification')

    # Foreign Keys
    period_id = data.get('period_id')
    period = None
    if not data.get('period') and period_id:
        period = Period.query.filter(Period.id == period_id).one()
    elif data.get('period'):
        period = add_period(data.get('period'))

    days_id = data.get('days_id')
    days = None
    if not data.get('period') and days_id:
        days = Days.query.filter(Days.id == days_id).one()
    elif data.get('days_id'):
        days = add_days(data.get('days_id'))

    forecast = Forecast(address, notification, period, days, user_id)
    db.session.add(forecast)
    db.session.commit()
    return forecast


def add_period(data):
    time_from = data.get('from')
    time_to = data.get('to')

    period = Period(time_from, time_to)
    db.session.add(period)
    db.session.commit()
    return period


def add_days(data):
    sunday = data.get('sunday')
    monday = data.get('monday')
    tuesday = data.get('tuesday')
    wednesday = data.get('wednesday')
    thursday = data.get('thursday')
    friday = data.get('friday')
    saturday = data.get('saturday')

    days = Days(sunday, monday, tuesday, wednesday, thursday, friday, saturday)
    db.session.add(days)
    db.session.commit()
    return days


def delete_user(user_id):
    post = User.query.filter(User.id == user_id).one()
    db.session.delete(post)
    db.session.commit()
