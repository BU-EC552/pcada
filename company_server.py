from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd

app = Flask(__name__)

@app.route('/company/<id>')
def get_company_data(id):
    main_data = pd.read_csv("comp" + str(id) + "_main.csv")
    main_data = main_data.to_dict()

    fragment_data = pd.read_csv("comp" + str(id) + "_fragment_cost.csv")
    fragment_data = fragment_data.to_dict()

    plasmid_data = pd.read_csv("comp" + str(id) + "_plasmid_cost.csv")
    plasmid_data = plasmid_data.to_dict()

    return {'main' : main_data, 'fragment' : fragment_data, 'plasmid' : plasmid_data}, 200

'''class Company(Resource):

    def get(self):
        name = flask.request.args.get('id', default = 0, type = int)
        #name = "comp" + str(id)
        #main_data = pd.read_csv(name + "_main.csv")
        #main_data = main_data.to_dict()

        #fragment_data = pd.read_csv(name + "_fragment.csv")
        #fragment_data = fragment_data.to_dict()

        #plasmid_data = pd.read_csv(name + "_plasmid.csv")
        #plasmid_data = plasmid_data.to_dict()

        return name, 200
        #return {'main' : main_data}, 200

class Users(Resource):
    # GET, POST, DELETE
    def get(self):
        data = pd.read_csv('users.csv')
        data = data.to_dict()
        return {'data': data}, 200

class Locations(Resource):
    pass
'''

if __name__ == '__main__':
    app.run()

#if __name__ == '__main__':
#    print("SALVE MUNDI")
#
#    app = Flask(__name__)
#    api = Api(app)
#    
#    api.add_resource(Company, '/company')#

 #   api.add_resource(Users, '/users')
 #   api.add_resource(Locations, '/locations')

 #   app.run()