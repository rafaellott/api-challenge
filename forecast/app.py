# coding: utf-8
from os import path
from flask import Flask, Blueprint
from forecast.api.v1.resources import user_namespace
from forecast.api import api
from forecast.database import db


def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'


def configure_api(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', 'forecast', url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(user_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)
    db.create_all(app=flask_app)


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
    configure_api(flask_app=app)

    return app
