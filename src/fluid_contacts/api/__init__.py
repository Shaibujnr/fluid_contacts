from flask import Blueprint
from flask_restful import Api
from .resources import SignupResource, SigninResource

blueprint = Blueprint("bp", __name__)
user_api = Api(blueprint, prefix="/user")
api = Api(blueprint)

user_api.add_resource(SignupResource, "/signup")
user_api.add_resource(SigninResource, "/signin")
