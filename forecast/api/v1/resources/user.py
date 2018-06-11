from flask import request
from flask_restplus import Resource

from forecast.api import api
from forecast.api.v1.controllers import add_user, delete_user
from forecast.api.v1.parsers import pagination_arguments
from forecast.api.v1.serializers import (
    user_serializer, user_page, forecast_serializer
)
from forecast.database.models import User, Forecast

ns = api.namespace('users', description='Users operations')

# Todo
# Users = {
#     '1': {
#         'name': 'Fulano Beltrano',
#         'forecast': [
#             {
#                 'address': 'Rua Marshmallow',
#                 'period': {
#                     'from': '08:00',
#                     'to': '19:00'
#                 },
#                 'days': {
#                     'sunday': True,
#                     'monday': True,
#                     'tuesday': True,
#                     'wednesday': True,
#                     'thursday': True,
#                     'friday': False,
#                     'saturday': False
#                 },
#                 'notification': '07:00'
#             }
#         ]
#     },
#     '2': {
#         'name': 'Ciclano Beltrano',
#         'forecast': [
#             {
#                 'address': 'Rua Oreo',
#                 'period': {
#                     'from': '22:00',
#                     'to': '06:00'
#                 },
#                 'days': {
#                     'sunday': True,
#                     'monday': True,
#                     'tuesday': True,
#                     'wednesday': True,
#                     'thursday': True,
#                     'friday': False,
#                     'saturday': False
#                 },
#                 'notification': '21:00'
#             }
#         ]
#     }
# }


@ns.route('/')
class UserCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(user_page)
    def get(self):

        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        user_query = User.query
        posts_page = user_query.paginate(page, per_page, error_out=False)
        return posts_page

    @api.expect(user_serializer)
    def post(self):
        add_user(request.json)
        return '', 201


@ns.route('/<int:user_id>')
@api.response(404, 'User not found.')
class USerItem(Resource):

    @api.marshal_with(user_serializer)
    def get(self, user_id):
        return User.query.filter(User.id == user_id).one()

    def delete(self, user_id):
        return delete_user(user_id), 204

    # TODO
    def put(self, user_id):
        raise NotImplementedError("method not implemented")
        # parser = reqparse.RequestParser()
        # parser.add_argument('name')
        # args = parser.parse_args()
        # user = {'name': args['name'], '...': '...'}
        # Users[user_id] = user
        # return '', 200


@ns.route('/<int:user_id>/forecast/')
@api.response(404, 'Forecast not found.')
class ForecastCollection(Resource):

    @api.marshal_with(forecast_serializer)
    def get(self, user_id):
        return Forecast.query.filter(Forecast.user_id == user_id).all()


@ns.route('/<int:user_id>/forecast/<int:forecast_id>')
@api.response(404, 'Forecast not found.')
class ForecastCollection(Resource):

    def get(self, user_id, forecast_id):
        pass

    def delete(self, user_id, forecast_id):
        return delete_forecast(user_id), 204
