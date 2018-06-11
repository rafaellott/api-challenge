from flask_restful import reqparse, Resource


# Todo
Users = {
    '1': {
        'name': 'Fulano Beltrano',
        'forecast': [
            {
                'address': 'Rua Marshmallow',
                'period': {
                    'from': '08:00',
                    'to': '19:00'
                },
                'days': {
                    'sunday': True,
                    'monday': True,
                    'tuesday': True,
                    'wednesday': True,
                    'thursday': True,
                    'friday': False,
                    'saturday': False
                },
                'notification': '07:00'
            }
        ]
    },
    '2': {
        'name': 'Ciclano Beltrano',
        'forecast': [
            {
                'address': 'Rua Oreo',
                'period': {
                    'from': '22:00',
                    'to': '06:00'
                },
                'days': {
                    'sunday': True,
                    'monday': True,
                    'tuesday': True,
                    'wednesday': True,
                    'thursday': True,
                    'friday': False,
                    'saturday': False
                },
                'notification': '21:00'
            }
        ]
    }
}


# Todo
class User(Resource):
    def get(self, user_id):
        return Users[user_id]

    def delete(self, user_id):
        del Users[user_id]
        return '', 204

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        user = {'name': args['name'], '...': '...'}
        Users[user_id] = user
        return user, 200
