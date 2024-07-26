from flask import Flask, request, jsonify, send_from_directory
import util

app = Flask(__name__, static_folder='../client', static_url_path='')

@app.route("/")
def home():
    return send_from_directory('../client', 'index.html')

@app.route("/get_location_names")
def get_location_names():
    locations = util.get_location_names()
    return jsonify({'locations': locations})

@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    estimated_price = util.get_estimate_price(location, total_sqft, bhk, bath)
    return jsonify({'estimated_price': estimated_price})

if __name__ == "__main__":
    util.load_saved_artifacts_()
    app.run(debug=True)
