#This programming language sucks balls
#
"""
            o_           
         .-"  ".          
       ."    _-'-""--o        
      J    ,"" _      ".
   .-",___,)____)___),-'

"""

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

currentBearing = 0


class doMovement(Resource):
    def get(self):
        distance = request.args.get('distance')
        time = request.args.get('time')
        speed = request.args.get('speed')
        return {
            'distance': distance,
            'time': time,
            'speed': speed,
            }
    
class doRotation(Resource):
    def get(self):
        bearing = request.args.get('bearing')
        speed = request.args.get('speed')
        currentBearing = bearing
        return {
            'bearing': bearing,
            'speed': speed,
            }
class getBearing(Resource):
    def get(self):
        return {
            'bearing': currentBearing,
            }

api.add_resource(doMovement, '/doMovement')
api.add_resource(doRotation, '/doRotation')
api.add_resource(getBearing, '/getBearing')
if __name__ == '__main__':
    app.run(debug=True, port=3002)
