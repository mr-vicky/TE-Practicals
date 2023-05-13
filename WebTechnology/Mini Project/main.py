from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from cloud import CloudDB
import csv
import base64
import io
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
api = Api(app)
CORS(app)

class UserRegister(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')   

    def post(self):
        data = self.parser.parse_args()
        output, result = CloudDB().insert_user(password=data['password'], email=data['email'])
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

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')

@app.route('/')
def display_data():
    # Read the CSV file and extract the data
    with open('fide_historical.csv', 'r') as file:
        data = list(csv.reader(file))
    
    # Format the data for display on the HTML page
    formatted_data = ''
    i = 0
    max = 11
    for row in data:
        if i == max:
            break
        if i == 0:
            for cell in row:
                formatted_data += f'<th>{cell}</th>'
            formatted_data += '</thead>'
        else:
            formatted_data += '<body><tr>'
            for cell in row:
                formatted_data += f'<td>{cell}</td>'
            formatted_data += '</tr>'
        i+=1
    
    df = pd.read_csv('fide_historical.csv')
    values = 10
    df = df.head(values)
    grouped = df.groupby('country')['rating'].sum()

    fig, ax = plt.subplots()
    ax.bar(grouped.index, grouped.values)

    ax.set_title('Bar Graph')
    ax.set_xlabel('Country')
    ax.set_ylabel('Rank')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    image_data = base64.b64encode(buffer.getvalue()).decode()
    bargraph = f'data:image/png;base64,{image_data}'

    
    # Render the HTML template and pass in the formatted data
    return render_template('index.html', data=formatted_data, image = bargraph)

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5001,
        host='0.0.0.0'
    )