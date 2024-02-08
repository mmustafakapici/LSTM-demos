import flask
import os
import json

app = flask.Flask(__name__)

@app.route('/')

def forecasts():
    with open('datas/combined_forecasts_json/ALL_combined_forecasts.json') as f:
        forecasts = json.load(f)
    return forecasts

if __name__ == '__main__':
    app.run()