import pandas as pd

URLS = {'president': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/pres110408.aspx',
        'attorney general': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/attGen110408.aspx',
        'house rep': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/congress110408.aspx',
        'state senate': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/ohSenate_110408.aspx',
        'state house': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/ohRep_110408.aspx',
        'president at-large': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/prpresal.aspx'
        }


def make_president_df():
    df = pd.read_html(URLS['president'])[0]
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])

    df.columns = ['county'] + list(df.columns[1:])
    df_ = pd.melt(df, id_vars=['county'], value_vars=list(df.columns[1:]))
    party_df = df_[pd.isnull(df_['county'])][['variable','value']]
    party_df.columns = ['candidate', 'party']
    df_.columns = ['county', 'candidate', 'votes']
    df_ = df_.dropna(subset=['county'])
    df_ = pd.merge(df_, party_df, how='left')
    df_['candidate'] = df_['candidate'].str.rstrip(' *')
    df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
    df_['candidate'] = df_['candidate'].str.rstrip('()')
    df_['office'] = 'President'
    president_df = df_

    return president_df

def make_president_AL_df():
    df = pd.read_html(URLS['president at-large'])[0]
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df.columns = ['county'] + list(df.columns[1:])
    df_ = pd.melt(df, id_vars=['county'], value_vars=list(df.columns[1:]))
    df_.columns = ['county', 'candidate', 'votes']
    df_ = df_.dropna(subset=['county'])
    df_['party'] = 'Republican'
    df_['candidate'] = df_['candidate'].str.lstrip('*')
    
    df_['office'] = 'President'
    president_df = df_

    return president_df


def make_attorney_df():
    df = pd.read_html(URLS['attorney general'])[0]
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])

    df.columns = ['county'] + list(df.columns[1:])
    df_ = pd.melt(df, id_vars=['county'], value_vars=list(df.columns[1:]))
    party_df = df_[pd.isnull(df_['county'])][['variable','value']]
    party_df.columns = ['candidate', 'party']
    df_.columns = ['county', 'candidate', 'votes']
    df_ = df_.dropna(subset=['county'])
    df_ = pd.merge(df_, party_df, how='left')
    df_['candidate'] = df_['candidate'].str.rstrip(' *')
    df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
    df_['candidate'] = df_['candidate'].str.rstrip('()')
    
    df_['office'] = 'Attorney General'
    attorney_df = df_

    return attorney_df

def make_state_representative_df():
    df = pd.read_html(URLS['state house'])[0]
    df.columns = ['county',
                  'candidate1', 'candidate2', 'candidate3']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('State Representative')].index.tolist()

    representative_df = pd.DataFrame()
    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        party_df = df_[df_['county'] == ''][['variable','value']]
        party_df.columns = ['candidate', 'party']
        df_.columns = ['county', 'candidate', 'votes']
        df_ = df_[df_['county'] != '']


        df_ = pd.merge(df_, party_df, how='left')
        df_['candidate'] = df_['candidate'].str.rstrip(' *')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['office'] = 'State Representative'
        representative_df = representative_df.append(df_)

    return representative_df

def make_USrepresentative_df():
    df = pd.read_html(URLS['house rep'])[0]
    df.columns = ['county', 'candidate1', 'candidate2',
                  'candidate3', 'candidate4', 'candidate5']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('U.S. Representative')].index.tolist()

    representative_df = pd.DataFrame()
    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        party_df = df_[df_['county'] == ''][['variable','value']]
        party_df.columns = ['candidate', 'party']
        df_.columns = ['county', 'candidate', 'votes']
        df_ = df_[df_['county'] != '']


        df_ = pd.merge(df_, party_df, how='left')
        df_['candidate'] = df_['candidate'].str.rstrip(' *')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['office'] = 'US Representative'
        representative_df = representative_df.append(df_)

    return representative_df

def make_state_senate_df():
    df = pd.read_html(URLS['state senate'])[0]
    df.columns = ['county',
                  'candidate1', 'candidate2', 'candidate3']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('State Senate')].index.tolist()

    representative_df = pd.DataFrame()
    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        party_df = df_[df_['county'] == ''][['variable','value']]
        party_df.columns = ['candidate', 'party']
        df_.columns = ['county', 'candidate', 'votes']
        df_ = df_[df_['county'] != '']


        df_ = pd.merge(df_, party_df, how='left')
        df_['candidate'] = df_['candidate'].str.rstrip(' *')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['office'] = 'State Senate'
        representative_df = representative_df.append(df_)

    return representative_df

def make_results():
    president_df = make_president_df()
    attorney_df = make_attorney_df()
    state_representative_df = make_state_representative_df()
    us_representative_df = make_USrepresentative_df()
    senate_df = make_state_senate_df()

    dfs = [president_df, attorney_df, state_representative_df,
           us_representative_df, senate_df]

    results = pd.DataFrame()
    for df in dfs:
        results = results.append(df)
    results = results[~results['county'].str.contains('Total')]
    results = results[~results['county'].str.contains('Percentage')]
    results['county'] = results['county'].str.rstrip(' **')
    results['county'] = results['county'].str.rstrip(' *')
    return results

results = make_results()
results.to_csv('20081104__oh__general.csv', index=False)

