import json
import csv

def load_districts():
    with open('county_crosswalk.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return [x for x in reader]
