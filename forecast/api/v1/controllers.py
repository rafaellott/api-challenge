import csv

from sqlalchemy.orm.exc import NoResultFound

from forecast.database import db
from forecast.database.models import User, Forecast, Period, Days


def add_user(data):
    name = data.get('name')
    if not name:
        raise AttributeError("required field 'name' not given")

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
    user = User.query.filter(User.id == user_id).one()
    delete_forecast(user_id=user.id)
    db.session.delete(user)
    db.session.commit()


################
# ## FORECAST ##
################
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
    if not data.get('days') and days_id:
        days = Days.query.filter(Days.id == days_id).one()
    elif data.get('days'):
        days = add_days(data.get('days'))

    forecast = Forecast(address, notification, period, days, user_id)
    db.session.add(forecast)
    db.session.commit()
    return forecast


def delete_forecast(user_id, forecast_id=None):
    forecast_query = Forecast.query.filter(Forecast.user_id == user_id)
    if forecast_id:
        forecast_query = forecast_query.filter(Forecast.id == forecast_id)

    for forecast in forecast_query.all():
        db.session.delete(forecast)
    db.session.commit()


def export_to_csv(path):
    outfile = open(path, 'w')
    outcsv = csv.writer(outfile)
    records = Forecast.query.all()
    outcsv.writerow([
        'id', 'name', 'forecast_id', 'address', 'period_from',
        'period_to', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday',
        'friday', 'saturday', 'notification'
    ])
    for record in records:
        outcsv.writerow([
            record.user.id, record.user.name, record.address,
            record.period.time_from, record.period.time_to,
            record.days.sunday, record.days.monday, record.days.tuesday,
            record.days.wednesday, record.days.thursday, record.days.friday,
            record.days.saturday, record.notification
        ])


def import_from_csv(path):
    pass
