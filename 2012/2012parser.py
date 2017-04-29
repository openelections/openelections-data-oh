import pandas as pd

#county,Precinct Name,Precinct Code,office,district,party,candidate,votes

df = pd.read_csv('2012precinct.txt', sep='\t')

#df = df.fillna(0)

df2 = pd.melt(df, id_vars=['COUNTY_NAME', 'PRECINCT_CODE', 'PRECINCT_NAME'],
              value_vars=list(df.columns.values[14:]))

df2[['office', 'district', 'candidate', '']] = df2['variable'].str.split('-', expand=True)
df3 = df2[df2['office'].isin(['President ', 'State Senate ',
                              'State House of Representatives ',
                              'U.S. House of Representatives '])]
df3['party'] = df3['district'].str.extract('\((.*?)\)')
df3['district'] = df3['district'].str.split(' ', expand=True)[2]
df3.columns = ['county', 'Precinct Code', 'Precinct Name', '1',
               'votes', 'office', 'district', 'candidate', '2',
               'party']
df3 = df3.drop(['1', '2'], 1)

df4 = df2[df2['office'].str.startswith('U.S. Senate')]
df4['party'] = df4['office'].str.extract('\((.*?)\)')
df4['office'] = 'U.S. Senate'
df4['candidate'] = df4['district']
df4['district'] = ''
df4.columns = ['county', 'Precinct Code', 'Precinct Name', '1', 'votes', 'office', 'district', 'candidate', '2', 'party']
df4 = df4.drop(['1', '2'], 1)

df5 = pd.concat([df3, df4])
df5 = df5[df5['votes'] != 0]
df5 = df5.dropna()
df5.to_csv('20121106__oh__general__precinct.csv')
