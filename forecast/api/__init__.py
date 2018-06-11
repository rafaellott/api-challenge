from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import Api

api = Api(
    version='1.0', title='Forecast API',
    description='A simple forecast notification API'
)


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    return (
        {'message': 'No result found for database query.'},
        404
    )
