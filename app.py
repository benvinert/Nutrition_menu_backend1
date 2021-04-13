from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import requests
import json


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/<food_id>')
@cross_origin()
def home(food_id):
    foodValues = requests.post(
        "https://www.goleango.com/calculators/nutrition_calculator/utils/get_hebrew_nutritional_value_for_food_id_json.php", data={'food_id': food_id})
    jsonob = json.loads(foodValues.text)
    print(jsonob)
    #   0 = Calories ,1 =Protein , 2 = Fat,3 = Carbs,4 = Collesterol, 5 = Fiber
    foodValuesSerialize = []
    for food in jsonob:
        if(food['id'] != "223"):
            foodValuesSerialize.append(food['value'])
    return jsonify(foodValuesSerialize)


if __name__ == "__main__":
    app.run(debug=True)
