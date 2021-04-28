from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd

app = Flask(__name__)

# Mock API request to company id - retrieve relevant data from CSVs, convert
# data to dictinary, and then send all the data back to the calling module.
# Adapted from https://pythonbasics.org/flask-http-methods/, 
# https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f
@app.route('/company/<id>')
def get_company_data(id):
    main_data = pd.read_csv("comp" + str(id) + "_main.csv")
    main_data = main_data.to_dict()

    fragment_data = pd.read_csv("comp" + str(id) + "_fragment_cost.csv")
    fragment_data = fragment_data.to_dict()

    plasmid_data = pd.read_csv("comp" + str(id) + "_plasmid_cost.csv")
    plasmid_data = plasmid_data.to_dict()

    return {'main' : main_data, 'fragment' : fragment_data, 'plasmid' : plasmid_data}, 200

if __name__ == '__main__':
    app.run()
