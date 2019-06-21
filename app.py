import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def apicall():
	"""API Call
	
	y predict array (sent as a payload) from API Call
	"""
	try:
		test_json = request.get_json()
		test = pd.read_json(test_json, orient='values')


	except Exception as e:
		raise e
	
	
	if test.empty:
		return(bad_request())
	else:

		answer = 5
		
		responses = jsonify(predictions=final_predictions.to_json(orient="values"))
		responses.status_code = 200

		return (responses)


@app.errorhandler(400)
def bad_request(error=None):
	message = {
			'status': 400,
			'message': 'Bad Request: ' + request.url + '--> Please check your data payload...',
	}
	resp = jsonify(message)
	resp.status_code = 400

	return resp
