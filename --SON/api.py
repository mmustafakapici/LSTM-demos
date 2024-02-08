import os
import flask 
import json

# datas/combined_forecasts_json/{ticker}_combined_forecast.json
# burada {ticker} yerine herhangi bir hisse kodu gelebilir
# örneğin: AAPL_combined_forecast.json
# bunların hepsini oku ve her bir tickeri bir endpoint olarak ekle

app = flask.Flask(__name__)


# datas/tickers.json tickerlerin bir listesini içerir
with open('datas/tickers.json') as f:
    tickers = json.load(f)
    
@app.route('/')
def index():
    return 'Welcome to the API'

@app.route('/tickers')

def get_tickers():
    return tickers


@app.route('/<ticker>')
def forecasts(ticker):
    with open(f'datas/combined_forecasts_json/{ticker}_combined_forecast.json') as f:
        forecasts = json.load(f)
    return forecasts

if __name__ == '__main__':
    app.run()
