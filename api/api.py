import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>IOT API</h1><p>This site is a prototype API for IOT sensing, namely the DHT11 for now.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/dht11', methods=['POST'])
def api_add():
	req_data = request.get_json()
	temp = req_data['temp']
	humidity = req_data['humidity']
	print(temp, humidity)
	response = {"status":"success"}
	return response, 200


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()








