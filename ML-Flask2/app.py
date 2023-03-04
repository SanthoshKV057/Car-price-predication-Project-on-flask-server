import numpy as np
from flask import Flask, request, jsonify, render_template,send_from_directory
import pickle
import locale

app=Flask(__name__)
model=pickle.load(open('D:/PROJECTS EDIT/ML-Flask2/models/model.pkl','rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method=='POST':
		features=[int(i) for i in request.form.values()]
		final_features=[np.array(features)]
		prediction=model.predict(final_features)
		output=int(round(prediction[0],2))
		

		# set the locale to India
		locale.setlocale(locale.LC_ALL, 'en_IN')

		
		rupees = locale.currency(output, grouping=True)


	return render_template('index.html',prediction_text='CAR PRICE IS {}'.format(rupees))


if __name__=='__main__':
	app.run(debug=True)