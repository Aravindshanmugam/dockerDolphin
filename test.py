# # seed the pseudorandom number generator
# from random import seed
# from random import random
# # seed random number generator
# seed(1)
# # generate some random numbers
# print(random(), random(), random())
# # reset the seed
# seed(1)
# # generate some random numbers
# print(random(), random(), random())

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)

class Users(Resource):
    # methods go here
    def get(self):
        return {'key':'hello'}, 200
    
class Locations(Resource):
    # methods go here
    pass
    
api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations
if __name__ == '__main__':
    app.run()  # run our Flask app