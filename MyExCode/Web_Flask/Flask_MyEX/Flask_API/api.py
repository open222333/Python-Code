from flask import Flask
from flask import request
from flask.json import jsonify


app = Flask(__name__)
app.config["DEBUG"] = True
#  Json以ASCII編碼呈現 關閉則以utf-8呈現
app.config['JSON_AS_ASCII'] = False


# test data
tpe = {
    "id": 0,
    "city_name": "台北",
    "country_name": "台灣",
    "is_capital": True,
    "location": {
        "longitude": 121.569649,
        "latitude": 25.036786
    }
}
nyc = {
    "id": 1,
    "city_name": "紐約",
    "country_name": "美國",
    "is_capital": False,
    "location": {
        "longitude": -74.004364,
        "latitude": 40.710405
    }
}
ldn = {
    "id": 2,
    "city_name": "倫敦",
    "country_name": "英國",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}

cities = [tpe, nyc, ldn]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"


@app.route('/cities/all', methods=['GET'])
def cities_all():
    return jsonify(cities)


# api
@app.route('/cities', methods=['GET'])
def city_name():
    if 'city_name' in request.args:
        city_name = request.args['city_name']
    else:
        return 'Error, no city_name'

    results = []
    for city in cities:
        if city['city_name'] == city_name:
            results.append(city)

    # jsonify(dict)
    return jsonify(results)


app.run()
