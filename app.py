import json
from flask import Flask
from flask_cors import CORS
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

app = Flask(__name__)
CORS(app)


@app.route("/api/locations")
def getLocations():
    df = pd.read_csv("./collections/1979_sm_locations.csv")
    return pd.DataFrame(df).to_json()

@app.route("/api/craters")
def getCreaters():
    df = pd.read_csv("./collections/moon_features.csv")
    return pd.DataFrame(df).to_json()

@app.route("/api/centers")
def getKMeans():
    centers = list([[-22.45454545, -64.54545455],
       [ 30.63636364,  51.81818182],
       [ 49.6       , -23.4       ]])
    return centers
   



if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
