import pickle
from flask import Flask,render_template,jsonify,url_for,request
import numpy as np
import pandas as pd
import os


app = Flask(__name__)
## load model
model = pickle.load(open("california.pkl",'rb'))
scaler = pickle.load(open("scaler.pkl",'rb'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict_api',methods = ['post'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    pred_data = model.predict(new_data)
    print(pred_data[0])
    return jsonify(pred_data[0])

@app.route('/predict',methods = ['post'])
def predict():
    data = [float(x) for x in  request.form.values()]
    scaled = scaler.transform(np.array(data).reshape(1,-1))
    pred_data = model.predict(scaled)[0]
    return render_template('home.html',prediction_text = "the price of the house is approximate {}".format(pred_data))




if __name__ == "__main__":

    app.run(debug=True)
