from flask import Blueprint
from flask_restful import Api
from .resources import (
    SignupResource,
    SigninResource,
    ContactCollectionResource,
    ContactResource,
    StarredContactCollectionResource,
    StarredContactResource,
    UnstarredContactResource,
)

blueprint = Blueprint("bp", __name__)
user_api = Api(blueprint, prefix="/user")
api = Api(blueprint)

user_api.add_resource(SignupResource, "/signup")
user_api.add_resource(SigninResource, "/signin")
api.add_resource(ContactCollectionResource, "/contact")
api.add_resource(ContactResource, "/contact/<int:contact_id>")
api.add_resource(StarredContactCollectionResource, "/contact/star")
api.add_resource(StarredContactResource, "/contact/<int:contact_id>/star")
api.add_resource(UnstarredContactResource, "/contact/<int:contact_id>/unstar")
