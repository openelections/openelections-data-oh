import json
from csvkit import unicsv

def load_districts():
    with open('county_crosswalk.csv', 'rb') as csvfile:
        reader = unicsv.UnicodeCSVDictReader(csvfile)
        return [x for x in reader]
