import flask
from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from api.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

# app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# db.init_app(app)


@bp.route('/', methods=['GET'])
def home():
    return "<h1>IOT API</h1><p>This site is a prototype API for IOT sensing, namely the DHT11 for now.</p>"

@bp.route('/v1/resources/dht11', methods=['POST'])
def api_add():
	req_data = request.get_json()
	temp = req_data['temp']
	humidity = req_data['humidity']
	print(temp, humidity)

	db = get_db()
	error = None
	response = {"status":"failure"}

	if not temp:
		error = "Temp is required"
	elif not humidity:
		error = "humidity is required"
	
	if error is None:
		db.execute(
			'INSERT INTO sensor_data (temp, humidity) values (?, ?)', (temp, humidity)
		)
		db.commit()
		response = {"status":"success"}

	return response, 200

@bp.route('/v1/resources/dht11', methods=['GET'])
def api_list():
	db = get_db()
	data = db.execute(
		'SELECT * from sensor_data'
	).fetchall()
	return render_template('api/index.html', data=data)

@bp.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# app.run()








