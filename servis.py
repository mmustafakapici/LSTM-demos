
from flask import Flask, jsonify
import json

app = Flask(__name__)

# JSON dosyasını okuma
with open('future_forecast.json', 'r') as file:
    data = json.load(file)

# Anasayfa route'u
@app.route('/')
def home():
    return "Merhaba, Flask sunucusu çalışıyor!"

# JSON verisini döndüren route
@app.route('/data')
def get_data():
    return jsonify(data)

# Sunucuyu çalıştırma
if __name__ == '__main__':
    app.run(debug=True)
