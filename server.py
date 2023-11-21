from flask import Flask, render_template, request
from water_monitoring import get_station_data
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/result', methods=['GET'])
def get_station():
    station_name = request.args.get('station_name', '')
    station_data = get_station_data(station_name)
    return render_template(
        "result.html",
        title=station_data["title"],
        temp=station_data["temp"],
        salinity=station_data["salinity"],
        electcon=station_data["electcon"],
        oxygen=station_data["oxygen"],
        BOD=station_data["BOD"],
    )

if __name__  == '__main__':
    serve(app, host="0.0.0.0", port=8000)