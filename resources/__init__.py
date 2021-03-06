from datetime import datetime, timedelta
from enum import IntEnum
from flask import current_app, jsonify
from flask_cors import CORS
from flask_jwt_simple import JWTManager, get_jwt
from flask_restful import Api
from functools import wraps
from werkzeug.exceptions import HTTPException
from os import environ


def initialize_resources(application):
    api = Api(application)
    jwt = JWTManager(application)
    # Caso a aplicação não esteja rodando local, tirar o origins abaixo
    if not environ.get('CORS_URL', None):
        CORS(application, supports_credentials=True, origins="*")
    else:
        # so usar na produção o comando abaixo
        CORS(application, resources={
             r"*": {"origins": environ.get('CORS_URL')}})

    # Endpoints
    from resources.user_password_recovery import UserPasswordRecoveryResource
    from resources.authentication import AuthenticationResource
    from resources.user import UserResource
    from resources.user import UserDetailResource
    from resources.client import ClientResource
    from resources.client import ClientDetailResource
    from resources.schedule import ScheduleResource
    from resources.schedule import ScheduleDetailResource
    from resources.report import ReportResource
    from resources.report import ReportDetailResource
    from resources.available_times import AvailableTimesResource
    from resources.vehicle import VehicleResource

    api.add_resource(UserResource, '/api/user')
    api.add_resource(VehicleResource, '/api/vehicle')
    api.add_resource(UserDetailResource, '/api/user/<int:id>')
    api.add_resource(ClientResource, '/api/client')
    api.add_resource(ClientDetailResource, '/api/client/<int:id>')
    api.add_resource(ScheduleResource, '/api/schedule')
    api.add_resource(ScheduleDetailResource, '/api/schedule/<int:id>')
    api.add_resource(ReportResource, '/api/report')
    api.add_resource(ReportDetailResource, '/api/report/<int:id>')
    api.add_resource(AvailableTimesResource, '/api/available_times/<date>')
    api.add_resource(UserPasswordRecoveryResource, '/api/user/recovery')
    api.add_resource(AuthenticationResource, '/api/login')


class HttpCode(IntEnum):
    Ok = 200
    BadRequest = 400
    Unauthorized = 401
    Forbidden = 403
    NotFound = 404
