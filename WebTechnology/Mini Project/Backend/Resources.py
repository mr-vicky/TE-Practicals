from ai_model_resource.api import SuggestModel
#
from dsbda_module import Sentiment
#
from cloud_db import CloudDB
#
from flask_restful import Resource, reqparse, request
import base64
from PIL import Image
import io


class UserRegister(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('firstName', type=str, required=True, help='First Name is required')
        self.parser.add_argument('lastName', type=str, required=True, help='Last Name is required')
        self.parser.add_argument('username', type=str, required=True, help='Username is required')
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')   

    def post(self):
        data = self.parser.parse_args()
        output, result = CloudDB().insert_user(username=data['username'], password=data['password'], email=data['email'],firstName=data['firstName'],lastName=data['lastName'])
        return output



class UserLogin(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')

    def post(self):
        data = self.parser.parse_args()
        output, result = CloudDB().retrieve_user(email=data['email'], password=data['password'])
        return output


class GenerateImage(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('query', type=str, required=True, help='Query is required')  

    def post(self):
        data = self.parser.parse_args()
        query = data['query']
        sent = Sentiment().check_sentiment(user_input=query)
        if sent == -1 :
            with open('warning.jpg', 'rb') as f:
                image_bytes = f.read()
            b64_image = base64.b64encode(image_bytes)
            b64_image = 'data:image/jpeg;base64,' + b64_image.decode('utf-8')
            output = {'status': '-1','image': b64_image, 'query': query}
            return output
        b64_image = SuggestModel().generate_image(query)
        output = {'status': '1', 'image': b64_image, 'query': query}
        return output
