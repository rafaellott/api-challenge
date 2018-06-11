from datetime import datetime
from time import strptime

from forecast.database import db

str_to_time = lambda st: datetime(*strptime(st, '%H:%M')[:6]).time()


class Period(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_from = db.Column(db.Time)
    time_to = db.Column(db.Time)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __init__(self, time_from, time_to):
        self.time_from = str_to_time(time_from)
        self.time_to = str_to_time(time_to)

    def __repr__(self):
        return '<Period %r - %r>' % (self.time_from, self.time_to)


class Days(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sunday = db.Column(db.Boolean, default=False)
    monday = db.Column(db.Boolean, default=False)
    tuesday = db.Column(db.Boolean, default=False)
    wednesday = db.Column(db.Boolean, default=False)
    thursday = db.Column(db.Boolean, default=False)
    friday = db.Column(db.Boolean, default=False)
    saturday = db.Column(db.Boolean, default=False)

    def __init__(
        self, sunday, monday, tuesday, wednesday, thursday, friday, saturday
    ):
        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday

    def __repr__(self):
        return '<Days %r>' % self.id


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    forecast = db.relationship('Forecast', back_populates="user")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name


class Forecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100))
    notification = db.Column(db.Time)
    period_id = db.Column(db.Integer, db.ForeignKey('period.id'))
    period = db.relationship(
        'Period', backref=db.backref('periods', lazy='dynamic')
    )

    days_id = db.Column(db.Integer, db.ForeignKey('days.id'))
    days = db.relationship(
        'Days', backref=db.backref('week_days', lazy='dynamic')
    )

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    user = db.relationship("User", back_populates="forecast")

    def __init__(self, address, notification, period, days, user_id):
        self.address = address
        self.notification = str_to_time(notification)
        self.period = period
        self.days = days
        self.user_id = user_id

    def __repr__(self):
        return '<Forecast %r - %r>' % self.address
