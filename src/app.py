# coding: utf-8
from os import path
from flask import Flask
from flask_restful import Api
from api.v1.resources.user import User
from api.v1.resources.forecast import Forecast


def start_app(mode="Development"):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), "{}_instance".format(mode)
    )

    app = Flask(
        "forecast",
        instance_path=instance_path,
        instance_relative_config=True
    )
    app.config.from_object("ppc_busca.config.{}Config".format(mode))
    return app


def start_api(app):
    api = Api(app)
    api.add_resource(User, '/users/<user_id>')
    api.add_resource(Forecast, '/users/<user_id>/forecast/<forecast_id>')


def create_app():
    app = start_app()
    start_api(app=app)
    return app
