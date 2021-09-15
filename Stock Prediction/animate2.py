'''
@Author: Swapnil Bhoyar
@Date: 2021-09-14
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-09-14
@Title : Program for flask web application.
'''
from flask import Flask,render_template,url_for,request,redirect, make_response
import json
from flask import Flask, render_template, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from datetime import datetime
import Consumer

# print('count')
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/data', methods=["GET", "POST"])
def data():

    pred_price, actual_price, date_time = Consumer.StockPricePrediction(Consumer.LoadModel)
    date_time = int(datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S').strftime('%s')) * 1000

    data = [date_time, actual_price, pred_price]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response

if __name__ == "__main__":
    app.run(debug=True)