from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from Resources import UserRegister, UserLogin, GenerateImage


app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(GenerateImage, '/generate')

if __name__ == '__main__':
    
    app.run(
        debug=True,
        port=5001,
        host='0.0.0.0',
        use_reloader=False
    )