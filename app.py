from __future__ import print_function #for Python v2
from flask import Flask, request, json
import pandas
import sys
from shapely import geometry

app = Flask(__name__)

def point_in_shapefile(list_tuples, lng, lat):
    polygon_array = geometry.Polygon(list_tuples)
    p = geometry.Point(lng, lat)
    return polygon_array.contains(p)

def getPlace(lat, lng):
    df = pandas.read_json("states.json", lines=True)
    df['present'] = df['border'].apply(lambda x: point_in_shapefile(x, lng, lat))
    name = df[df['present'] == True]['state'].values[0] if df[df['present'] == True]['state'].count() > 0 else "NoneFound"
    return name
    
@app.route('/', methods=['POST'])
def index():
    try:
        #40.513799 -77.036133 Penlya
        #-122.402014, 48.225214 Washn
        if (request.headers['Content-Type'] == 'application/json'):
            lat = request.json.get('latitude')
            lng = request.json.get('longitude')
            place = getPlace(float(lat), float(lng))
            print(place, file=sys.stdout)
            return place 
    except Exception as e:
        print(str(e.message), file=sys.stderr)
    return "Error - Check the post data - longitude and latitude."

if __name__ == '__main__':
    app.run(debug=True,  port=8080)