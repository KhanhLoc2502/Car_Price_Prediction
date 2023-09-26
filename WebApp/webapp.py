from flask import Flask, redirect, url_for, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('bagging.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('predict.html',**locals())


@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    
    final_features = [np.array(int_features)]
    result = model.predict(final_features)
    output = int(result[0])
    return render_template('predict.html', prediction_text='Predicted Price {}'.format(output),**locals())

if __name__ == '__main__':
    app.run(debug=True)