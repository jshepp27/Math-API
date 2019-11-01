from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
    if (functionName == 'add' or functionName == 'subtract' or functionName == 'multiply'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        return 200
    elif (functionName == 'divide'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        elif int(postedData['y']) == 0:
            return 302
        return 200

class Add(Resource):
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()
    
        # Step 2: Verify validaity of posted data
        status_code = checkPostedData(postedData, "add")
        print(status_code)
        if (status_code != 200):
            retJson = {
                "Message": "An error occured",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # Step 3: Get posted data
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)

        # Step 2: Add the posted data
        ret = x+y

        # Step 3 return response to user
        retMap = {
            'Message': ret,
            'Status Code': status_code
        }
        return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()
    
        # Step 2: Verify validaity of posted data
        status_code = checkPostedData(postedData, "subtract")
        print(status_code)
        if (status_code != 200):
            retJson = {
                "Message": "An error occured",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # Step 3: Get posted data
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)

        # Step 2: Add the posted data
        ret = x-y

        # Step 3 return response to user
        retMap = {
            'Message': ret,
            'Status Code': status_code
        }
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()
    
        # Step 2: Verify validaity of posted data
        status_code = checkPostedData(postedData, "multiply")
        print(status_code)
        if (status_code != 200):
            retJson = {
                "Message": "An error occured",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # Step 3: Get posted data
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)

        # Step 2: Add the posted data
        ret = x*y

        # Step 3 return response to user
        retMap = {
            'Message': ret,
            'Status Code': status_code
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()
    
        # Step 2: Verify validaity of posted data
        status_code = checkPostedData(postedData, "divide")
        print(status_code)
        if (status_code != 200):
            retJson = {
                "Message": "An error occured",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # Step 3: Get posted data
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)

        # Step 2: Add the posted data
        ret = x/y

        # Step 3 return response to user
        retMap = {
            'Message': ret,
            'Status Code': status_code
        }
        return jsonify(retMap)

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

if __name__ == "__main__":
    app.run(debug=True)

