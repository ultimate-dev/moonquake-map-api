from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)


@app.route("/api/locations")
def getLocations():
    df = pd.read_csv("./collections/1979_sm_locations.csv")
    return pd.DataFrame(df).to_json()

@app.route("/api/craters")
def getCreaters():
    df = pd.read_csv("./collections/1979_sm_locations.csv")
    return pd.DataFrame(df).to_json()


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
