#! usr/bin/env python

from sys import argv
from os.path import exists
import json
import codecs

script, in_file, out_file = argv

data = json.load(open(in_file),'utf-8')

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["longitude"], d["latitude"]],
            },
        "properties" : d,
     } for d in data]
}


output = codecs.open(out_file, 'w','utf-8')
json.dump(geojson, output, ensure_ascii=False)

print geojson
