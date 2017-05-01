import pandas as pd

#county,Precinct Name,Precinct Code,office,district,party,candidate,votes

df = pd.read_csv('2010_primary_precinct.txt', sep='\t')

#df = df.fillna(0)

df2 = pd.melt(df, id_vars=['COUNTY NUMBER', 'STATE PRC CODE', 'PRECINCT NAME'],
              value_vars=list(df.columns.values[11:]))

df2[['office', 'candidate', '']] = df2['variable'].str.split(' - ', expand=True)
df2['party'] = df2['office'].str.extract('\((.*?)\)')
df2['office'] = df2['office'].str[:-4].str.strip()

df3 = df2[df2['office'].isin(['Governor/Lieutenant Governor', 'Attorney General',
                              'Auditor of State', 'Secretary of State',
                              'Treasurer of State'])]

df3.columns = ['county', 'Precinct Code', 'Precinct Name', '1',
               'votes', 'office', 'candidate', '2',
               'party']
df3 = df3.drop(['1', '2'], 1)

df2 = pd.melt(df, id_vars=['COUNTY NUMBER', 'STATE PRC CODE', 'PRECINCT NAME'],
              value_vars=list(df.columns.values[11:]))

df2[['office', 'district', 'candidate']] = df2['variable'].str.split(' - ', expand=True)
df2 = df2[df2['office'].isin(['State Senate', 'U.S. Representatives',
                        'State Representatives'])]
df2['party'] = df2['district'].str.extract('\((.*?)\)')
df2['district'] = df2['district'].str.split(' ', expand=True)[1]
df2.columns = ['county', 'Precinct Code', 'Precinct Name', '1',
               'votes', 'office', 'district', 'candidate',
               'party']
df2 = df2.drop(['1'], 1)

df4 = pd.concat([df2, df3])
df4 = df4[df4['votes'] != 0]
df4 = df4[~df4['Precinct Name'].str.contains('TOTAL')]
df4.to_csv('20100504__oh__primary__precinct.csv', index=False)

### General Election Data

df = pd.read_csv('2010_general_precinct.txt', sep='\t')

#df = df.fillna(0)

df2 = pd.melt(df, id_vars=['COUNTY NAME', 'PRECINCT_CODE', 'PRECINCT_NAME'],
              value_vars=list(df.columns.values[6:]))

df2['office'] = df2['variable'].str.split(' - ', expand=True)[0]

df3 = df2[df2['office'].isin(['Governor/Lieutenant Governor', 'Attorney General',
                              'Auditor of State', 'Secretary of State',
                              'Treasurer of State'])]

df3[['office', 'candidate']] = df3['variable'].str.split(' - ', expand=True)

df3.columns = ['county', 'Precinct Code', 'Precinct Name', '1',
               'votes', 'office', 'candidate']
df3 = df3.drop(['1'], 1)

df4 = df2[df2['office'].isin(['U.S. Representative',
                              'State Senate', 'State Representative'])]

df4[['office', 'district', 'candidate']] = df4['variable'].str.split(' - ', expand=True)
df4['district'] = df4['district'].str.split(' ', expand=True)[1]
df4.columns = ['county', 'Precinct Code', 'Precinct Name', '1',
               'votes', 'office', 'district', 'candidate']
df4 = df4.drop(['1'], 1)

df5 = pd.concat([df3, df4])
df5 = df5[df5['votes'] != 0]
df5 = df5.dropna(subset=['Precinct Name'])
df5 = df5[~df5['Precinct Name'].str.contains('TOTAL')]
df5.to_csv('20100504__oh__general__precinct.csv', index=False)
