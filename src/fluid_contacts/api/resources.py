from flask_restful import Resource, reqparse, fields, marshal
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from fluid_contacts import db
from ..models import User, Contact

signup_parser = reqparse.RequestParser()
signup_parser.add_argument('username', type=str, help="user name")
signup_parser.add_argument('email', type=str, help='user email')
signup_parser.add_argument('password', type=str, help='user password')


signin_parser = reqparse.RequestParser()
signin_parser.add_argument('username', type=str, help="enter username")
signin_parser.add_argument('password', type=str, help="user password")


contact_parser = reqparse.RequestParser()
contact_parser.add_argument("phonenumber")
contact_parser.add_argument("email")
contact_parser.add_argument("address")
contact_parser.add_argument("name")


contact_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'phonenumber': fields.String,
    'email': fields.String,
    'address': fields.String,
    'starred': fields.Boolean,
}


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
        # add new contact for the authenticated user
        username = get_jwt_identity()
        args = contact_parser.parse_args(strict=True)
        name = args['name']
        email = args['email']
        phonenumber = args['phonenumber']
        address = args['address']
        if not name or not email or not phonenumber or not address:
            return (
                dict(
                    message="name, phonenumber, email and address must be provided"
                ),
                400,
            )
        user = User.query.filter_by(username=username).first()
        if user is not None:
            contact = Contact(
                name=name,
                email=email,
                address=address,
                phonenumber=phonenumber,
                user_id=user.id,
            )
            db.session.add(contact)
            db.session.commit()
            return marshal(contact, contact_fields), 200
        return dict(message="user does not exist"), 400

    @jwt_required
    def get(self):
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()
        if user is not None:
            return marshal(user.contacts, contact_fields), 200
        return dict(message="User does not exist"), 400


class ContactResource(Resource):
    @jwt_required
    def get(self, contact_id):
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()
        if user:
            contact = Contact.query.get(contact_id)
            if contact:
                return marshal(contact, contact_fields), 200
            return (
                {"message": "contact with id %d does not exist" % contact_id},
                400,
            )
        return dict(message="User does not exist"), 400

    @jwt_required
    def patch(self, contact_id):
        username = get_jwt_identity()
        args = contact_parser.parse_args(strict=True)
        name = args['name']
        email = args['email']
        phonenumber = args['phonenumber']
        address = args['address']
        user = User.query.filter_by(username=username).first()
        if user:
            contact = Contact.query.get(contact_id)
            if contact:
                if name:
                    contact.name = name
                if email:
                    contact.email = email
                if phonenumber:
                    contact.phonenumber = phonenumber
                if address:
                    contact.address = address
                db.session.commit()
                return marshal(contact, contact_fields), 200
            return (
                {"message": "contact with id %d does not exist" % contact_id},
                400,
            )
        return dict(message="User does not exist"), 400

    @jwt_required
    def delete(self, contact_id):
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()
        if user:
            contact = Contact.query.get(contact_id)
            if contact:
                db.session.delete(contact)
                db.session.commit()
                return marshal(contact, contact_fields), 200
            return (
                {"message": "contact with id %d does not exist" % contact_id},
                400,
            )
        return dict(message="User does not exist"), 400
