# coding: utf-8
from os import path
from flask import Flask
from flask_restful import Api
from forecast.api.v1.resources import User
from forecast.api.v1.resources import Forecast


def start_api(app):
    api = Api(app)
    api.add_resource(User, '/api/v1/users/<user_id>')
    api.add_resource(Forecast, '/api/v1/users/<user_id>/forecast/<forecast_id>')


def create_app(mode="Development"):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), "{}_instance".format(mode)
    )
    app = Flask(
        "forecast",
        instance_path=instance_path,
        instance_relative_config=True
    )
    app.config.from_object("forecast.config.{}Config".format(mode))
    start_api(app=app)
    return app
