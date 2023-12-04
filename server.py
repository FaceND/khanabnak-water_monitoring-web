from flask import Flask, render_template, request, send_from_directory
from water_monitoring import get_station_data
from waitress import serve
import os
import warnings

warnings.filterwarnings("ignore")
app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/assets/images/icons'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

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
    print("\033[92m√\033[0m Compiled successfully.")
    serve(app, host="0.0.0.0", port=8000)