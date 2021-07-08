from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
import sys
import numpy as np
import json
from json import JSONEncoder

# Get your flask app object
app = Flask(__name__)

# Load model from local FS on server start
model_path = (r'./3/')
model = load_model(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict(features)
    return render_template('index.html', prediction="Estimated sine values: {}".format(prediction))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls through request
    '''
    data = request.get_json(force=True)
    features = [float(x) for x in data.values()]
    prediction = model.predict(features).tolist()
    return jsonify({'prediction':prediction})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
