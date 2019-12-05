import csv
from districts import load_districts

#COUNTIES = ['Adams','Allen','Ashland','Ashtabula','Athens','Auglaize','Belmont','Brown','Butler','Carroll','Champaign','Clark','Clermont','Clinton','Columbiana','Coshocton','Crawford','Cuyahoga','Darke','Defiance','Delaware','Erie','Fairfield','Fayette','Franklin','Fulton','Gallia','Geauga','Greene','Guernsey','Hamilton','Hancock','Hardin','Harrison','Henry','Highland','Hocking','Holmes','Huron','Jackson','Jefferson','Knox','Lake','Lawrence','Licking','Logan','Lorain','Lucas','Madison','Mahoning','Marion','Medina','Meigs','Mercer','Miami','Monroe','Montgomery','Morgan','Morrow','Muskingum','Noble','Ottawa','Paulding','Perry','Pickaway','Pike','Portage','Preble','Putnam','Richland','Ross','Sandusky','Scioto','Seneca','Shelby','Stark','Summit','Trumbull','Tuscarawas','Union','Van Wert','Vinton','Warren','Washington','Wayne','Williams','Wood','Wyandot']

COUNTIES = ['Delaware', 'Franklin', 'Licking', 'Marion', 'Morrow', 'Muskingum', 'Richland']

districts = load_districts()

with open('/Users/dwillis/Downloads/precinctgreen.csv', 'rb') as csvfile:
    filename = "20180508__oh__primary__precinct_g.csv"
    reader = unicsv.UnicodeCSVReader(csvfile)
    offices = next(reader)
    fixed_offices = ['Representative to Congress'] * 3
#        if office != '':
#            o = office.strip()
#            fixed_offices.append(office.strip())
#        else:
#            fixed_offices.append(o)
    headers = next(reader)
    fixed_cols = headers[0:8]
    fixed_cols.extend(['office', 'district', 'party', 'candidate', 'votes'])
    cands = headers[8:]
    l = list(reader)
    results = []
    for county in COUNTIES:
        county_districts = [d for d in districts if d['county'] == county]
        results = []
        filename = "20180807__oh__special__general__%s__precinct.csv" % county.lower()
        rows = [x for x in l if x[0] == county]
        for row in rows:
            county = row[0].strip()
            for idx, cand in enumerate(cands):
                if row[0] == 'Percentage' or row[0] == 'Total':
                    continue
                office = fixed_offices[idx]
                if ' - District' in office:
                    office, district = office.split(' - District')
                    office = office.strip()
                    district = district.strip()
                else:
                    district = '12'
                votes = row[idx+8]
                if office == 'President (district)' or office == 'Representative to Congress':
                    d = [int(x['district']) for x in county_districts if x['office'] == 'U.S. House']
                    if int(district[0:2]) in d:
                        results.append([county, row[1], row[2], row[3], row[4], row[5], row[6], office, district, party, cand, votes])
                elif office == 'State Representative':
                    d = [int(x['district']) for x in county_districts if x['office'] == 'State House']
                    if int(district[0:2]) in d:
                        results.append([county, row[1], row[2], row[3], row[4], row[5], row[6], office, district, party, cand.split(' (')[0].replace('  ', ' '), votes])
                elif office == 'State Senator':
                    d = [int(x['district']) for x in county_districts if x['office'] == 'State Senate']
                    if int(district[0:2]) in d:
                        results.append([county, row[1], row[2], row[3], row[4], row[5], row[6], office, district, party, cand.split(' (')[0].replace('  ', ' '), votes])
                elif office in ['President','U.S. Senator' ,'Governor and Lieutenant Governor', 'Attorney General', 'Auditor of State', 'Secretary of State', 'Treasurer of State']:
                    results.append([county, row[1], row[2], row[3], row[4], row[5], row[6], office, district, party, cand.split(' (')[0].replace('  ', ' '), votes])
                else:
                    continue

        with open(filename, 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fixed_cols)
            writer.writerows(results)
