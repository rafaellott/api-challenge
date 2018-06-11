# coding: utf-8
from flask import Flask, Blueprint
from os import path
import click
from forecast.api import api
from forecast.api.v1.resources import user_namespace
from forecast.database import db


def configure_api(flask_app):
    blueprint = Blueprint('api', 'forecast', url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(user_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)
    db.create_all(app=flask_app)


def add_command_line(app):

    @app.cli.command()
    @click.argument('path', default='/tmp/forecast.csv')
    def export_csv(path):
        from forecast.api.v1.controllers import export_to_csv
        export_to_csv(path)

    @app.cli.command()
    @click.argument('path', default='/tmp/forecast.csv')
    def import_csv(path):
        from forecast.api.v1.controllers import import_from_csv
        import_from_csv(path)


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

    add_command_line(app)

    return app
