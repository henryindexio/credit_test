import os
from flask import Flask, jsonify, request
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score

app = Flask(__name__)

@app.route('/', methods=['POST'])
def apicall():
	"""API Call
	
	y predict array (sent as a payload) from API Call
	"""
	try:
		y_pred_json = request.get_json()
		y_pred  = json.loads(array)
		
	except Exception as e:
		raise e
	
	
	if y_pred.empty:
		return(bad_request())
	else:

		y_test = pd.read_csv('http://www.sharecsv.com/dl/0603fc2a3fafaf03fe477ff9e5078e03/y_test.csv')
		f1 = f1_score(y_test,y_pred)
		recall = recall_score(y_test,y_pred)
		precision = precision_score(y_test,y_pred)
		accuracy = accuracy_score(y_test,y_pred)
		metrics = {'f1_score': f1, 'recall_score': recall, 'precision_score': precision, 'accuracy_score': accuracy}
		
		responses = jsonify(metrics)
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


if __name__ == '__main__':
    app.run(debug=True)
