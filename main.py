from flask import Flask
from flask_restful import Api, Resource, reqparse
from math import hypot
from flask_cors import CORS


# app = Flask("Desafio Cromai | Pitágoras")
app = Flask(__name__)
api = Api(app)
CORS(app)
parser = reqparse.RequestParser()


class Pitagoras(Resource):
    def post(self):
        parser.add_argument('opposite_side')
        parser.add_argument('adjacent_side')
        args = parser.parse_args()

        opposite_side = float(args['opposite_side'])
        adjacent_side = float(args['adjacent_side'])
        hypotenuse = hypot(opposite_side, adjacent_side)
        formatted_hypotenuse = float("{:.2f}".format(hypotenuse))
        return {"hypotenuse": formatted_hypotenuse}


api.add_resource(Pitagoras, "/calculate")

if __name__ == "__main__":
    app.run(debug=True)
