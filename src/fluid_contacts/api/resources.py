from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from ..models import db, User

signup_parser = reqparse.RequestParser()
signup_parser.add_argument('username', type=str, help="user name")
signup_parser.add_argument('email', type=str, help='user email')
signup_parser.add_argument('password', type=str, help='user password')


signin_parser = reqparse.RequestParser()
signin_parser.add_argument('username', type=str, help="enter username")
signin_parser.add_argument('password', type=str, help="user password")


class SignupResource(Resource):
    def post(self):
        args = signup_parser.parse_args(strict=True)
        username = args['username']
        email = args['email']
        password = args['password']
        if username is None or password is None or email is None:
            return (
                {
                    "message": "username, email and password fields must be provided"
                },
                400,
            )
        existing_user = (
            User.query.filter_by(username=username).first()
            or User.query.filter_by(email=email).first()
        )
        if existing_user:
            return {"message": "user already exists"}, 400
        user = User(username=username, email=email, password=password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return (
            {
                "message": "user created successfully",
                "token": create_access_token(identity=username),
            },
            200,
        )


class SigninResource(Resource):
    def post(self):
        args = signin_parser.parse_args(strict=True)
        username = args['username']
        password = args['password']
        if username is None or password is None:
            return (
                {"message": "username and password fields must be provided"},
                400,
            )
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            return (
                {
                    "message": "success",
                    "token": create_access_token(identity=username),
                },
                200,
            )
        return {"message": "authentication failed"}, 400


class ContactCollectionResource(Resource):
    @jwt_required
    def post(self):
        username = get_jwt_identity()
        return dict(message="Add a new contact for %s" % username)

    @jwt_required
    def get(self):
        username = get_jwt_identity()
        return dict(message="Read all contacts for %s" % username)


class ContactResource(Resource):
    @jwt_required
    def get(self, id):
        username = get_jwt_identity()
        return dict(message="get contact with id %d for %s" % (id, username))

    @jwt_required
    def patch(self, id):
        username = get_jwt_identity()
        return dict(
            message="update contact with id %d for %s" % (id, username)
        )

    @jwt_required
    def delete(self, id):
        username = get_jwt_identity()
        return dict(
            message="Delete contact with id %d for %s" % (id, username)
        )
