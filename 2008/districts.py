import pandas as pd

def scrape_districts():
    district_df = pd.DataFrame(columns=['County', 'District'])
    url = 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/pdusrep.aspx'
    df = pd.read_html(url)[0]
    df.columns = ['county', 'candidate1', 'candidate2',
                  'candidate3', 'candidate4', 'candidate5',
                  'candidate6']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('DISTRICT')].index.tolist()

    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        df_['county'] = df_['county'].str.rstrip(' **')
        for row in df_.iterrows():
            district_df = district_df.append({'County': row[1]['county'], 'District': split + 1}, ignore_index=True)
            print([row[1]['county'], split + 1])
    return district_df

if __name__ == '__main__':
    df = scrape_districts()
    df['District'] = df['District'].astype(int)
    df = df[~df['County'].str.contains('Total')]
    df = df[~df['County'].str.contains('Percentage')]
    df.to_csv('2008districts.csv', index=False)
    
