import json
<<<<<<< Updated upstream
import unicsv
=======
import csv
>>>>>>> Stashed changes

def load_districts():
    with open('county_crosswalk.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        return [x for x in reader]
