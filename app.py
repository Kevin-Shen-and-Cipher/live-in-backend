
from flask import Flask, render_template, request, jsonify,Response
import json
from get_house import get_house
from get_job import get_job
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
        return "Hello, test!"

@app.route("/house", methods=["POST"])
def get_house_ten():
        try:
                json1 = request.json
                address = json1["address"]
                area = (json1["area"])
                try:
                        multi_area = json1["multi-area"]
                except:
                        multi_area = None
                try:
                        multi_floor = json1["multi-floor"]
                except:
                        multi_floor = None
                try:
                        multi_notice = json1["multi-notice"]
                except:
                        multi_notice = None
                try:
                        multi_price = json1["multi-price"]
                except:
                        multi_price = None
                try:
                        multi_room = json1["multi-room"]
                except:
                        multi_room = None
                try:
                        option_set = json1["option"]
                except:
                        option_set = None
                try:
                        other = json1["other"]
                except:
                        other = None
                try:
                        rentKind = json1["rentKind"]
                except:
                        rentKind = None
                try:
                        shape = json1["shape"]
                except:
                        shape = None
                filter_data = {
                        "multi_area":multi_area,
                        "multi_floor": multi_floor,
                        "multi_notice": multi_notice,
                        "multi_price" : multi_price,
                        "multi_room" : multi_room,
                        "option_set" : option_set,
                        "other" : other,
                        "rentKind" : rentKind,
                        "shape" : shape,
                }
                return jsonify(get_house(address, area, filter_data))
        except Exception as e:
                print(e)
                return "fail"

@app.route("/job", methods=["POST"])
def get_job_function():
        json1 = request.json
        address = json1["address"]
        area = (json1["area"])
        filter_data = {
                "salary":json1["salary"],
                "job-exp": json1["job-tenure"],
                "working-hour": json1["working-hour"]
        }
        return jsonify(get_job(address, area, filter_data))


@app.errorhandler(404)
def not_found(error):
    print(str(error))
    return '404', 404

if __name__ == '__main__':
        app.run( port=5000)
