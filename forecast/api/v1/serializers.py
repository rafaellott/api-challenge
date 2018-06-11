from flask_restplus import fields
from forecast.api import api


forecast_period = api.model(
    'Forecast period',
    {
        'from': fields.String(
            required=True, description="Forecast period 'FROM'",
            attribute='time_from'
        ),
        'to': fields.String(
            required=True, description="Forecast period 'TO'",
            attribute='time_to'
        ),
    }
)

forecast_days = api.model(
    'Forecast days',
    {
        'sunday': fields.Boolean(default=False),
        'monday': fields.Boolean(default=False),
        'tuesday': fields.Boolean(default=False),
        'wednesday': fields.Boolean(default=False),
        'thursday': fields.Boolean(default=False),
        'friday': fields.Boolean(default=False),
        'saturday': fields.Boolean(default=False),
    }
)

forecast_serializer = api.model(
    'User forecast',
    {
        'id': fields.String(
            readOnly=True, description="The unique identifier of forecast"
        ),
        'address': fields.String(description="Forecast adress"),
        'period': fields.Nested(forecast_period, required=True),
        'days': fields.Nested(forecast_days, required=True),
        'notification': fields.String(required=True),
    }
)

user_serializer = api.model(
    'User',
    {
        'id': fields.String(
            readOnly=True, description="The unique identifier of user"
        ),
        'name': fields.String(
            required=True, description="Name of the user"
        ),
        'forecast': fields.List(fields.Nested(forecast_serializer))
    }
)

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(
        description='Number of items per page of results'
    ),
    'total': fields.Integer(description='Total number of results'),
})

user_page = api.inherit('Page of user list', pagination, {
    'items': fields.List(fields.Nested(user_serializer))
})

