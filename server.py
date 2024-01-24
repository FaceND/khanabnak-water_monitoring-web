from flask import Flask, render_template, request, send_from_directory, jsonify
from water_monitoring import get_station_data, get_all_station_data
from waitress import serve
import os
import warnings
from flask_cors import CORS

warnings.filterwarnings("ignore")
app = Flask(__name__)

# Allow CORS origin resource sharing
CORS(app)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/assets/images/icons'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
@app.route('/home')
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
    
@app.route('/api', methods=['GET'])
def api_get_all_station_data():
    app.json.sort_keys = False
    app.config['JSON_AS_ASCII'] = False
    data = get_all_station_data()
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/coastal_aquaculture_table')
def coastal_aquaculture_table():
    return render_template('/table/coastal_aquaculture_table.html')

@app.route('/growing_fruit_table')
def growing_fruit_table():
    return render_template('/table/growing_fruit_crops_table.html')

@app.route('/white_shrimp_table')
def white_shrimp_table():
    return render_template('/table/white_shrimp_table.html')

@app.route('/raising_fish_cage_table')
def raising_fish_table():
    return render_template('/table/raising_fish_cage_table.html')

if __name__  == '__main__':
    print("\033[92m√\033[0m Compiled successfully.")
    serve(app, host="0.0.0.0", port=8000)