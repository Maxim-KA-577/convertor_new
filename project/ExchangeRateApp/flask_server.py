from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route("/latest_data")
def latest_data():
    with open('serv/latest_rates.json', 'r') as lf:
        currency_data = lf.readline()
    return jsonify(currency_data)


@app.route("/usd")
def data_usd():
    with open('serv/historical_usd.json', 'r') as file:
        data_json = file.readline()
    resp = data_json
    return jsonify(resp)


@app.route("/eur")
def data_eur():
    with open('serv/historical_eur.json', 'r') as file:
        data_json = file.readline()
    resp = data_json
    return jsonify(resp)


@app.route("/kzt")
def data_kzt():
    with open('serv/historical_kzt.json', 'r') as file:
        data_json = file.readline()
    resp = data_json
    return jsonify(resp)


@app.route("/cny")
def data_cny():
    with open('serv/historical_cny.json', 'r') as file:
        data_json = file.readline()
    resp = data_json
    return jsonify(resp)


app.run(debug=True)












