#!/usr/bin/python
import sys
import pandas as pd
from shapely import geometry
def point_in_shapefile(list_tuples, lng, lat):
    polygon_array = geometry.Polygon(list_tuples)
    p = geometry.Point(lng, lat)
    return polygon_array.contains(p)

def getPlace(lat, lng):
    df = pd.read_json("states.json", lines=True)
    df['present'] = df['border'].apply(lambda x: point_in_shapefile(x, lng, lat))
    name = df[df['present'] == True]['state'].values[0] if df[df['present'] == True]['state'].count() > 0 else "NoneFound"
    return name
    
def main():
    try:
        #40.513799 -77.036133
        #40.6273817 -74.0241252
        print(getPlace(float(sys.argv[1]), float(sys.argv[2])))
    except Exception as e:
        print(e.message)
        print("Note that arguments are (Longitude followed by Latitude) in that order!")
        
if __name__ == '__main__':
    main()