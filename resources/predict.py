import pickle
import numpy as np
from flask_restful import Resource,request
from flask import render_template
import json

data_column = None
locations = None
bat_team = None
bowl_team = None
model = None

with open('./artifacts/columns.json','r') as f:
    data_column = json.load(f)['data_columns']
    locations = data_column[:31]
    bat_team  = data_column[31:39]
    bowl_team = data_column[39:47]

if model == None:
    with open('./artifacts/predict.pkl','rb') as f:
        model = pickle.load(f)

class Predict(Resource):

    def post(self):

        venue = request.form['venue']
        bat = request.form['bat']
        bowl = request.form['bowl']
        crun = int(request.form['crun'])
        cwic = int(request.form['cwic'])
        over = float(request.form['over'])
        frun = int(request.form['frun'])
        fwic = int(request.form['fwic'])

        try:
            venue_index = data_column.index(venue.lower())
        except:
            venue_index = -1

        try:
            bat_index = data_column.index(bat.lower())
        except:
            bat_index = -1
        
        try:
            bowl_index = data_column.index(bowl.lower())
        except:
            bowl_index = -1

        x = np.zeros(len(data_column))
    
        if venue_index>=0:
            x[venue_index]=1

        if bat_index>=0:
            x[bat_index]=1
    
        if bowl_index>=0:
            x[bowl_index]=1

        x[47] = crun
        x[48] = cwic
        x[49] = over
        x[50] = frun
        x[51] = fwic

        output = round(model.predict([x])[0],2)

        #output = str(output+' runs')

        #return render_template('home.html',pred="Predicted score fot this match is {} runs".format(output))
        return {'Predicted score fot this match is':output}





    

