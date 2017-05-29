import pandas as pd

URLS = {'dem_president': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/pdpresdistrict.aspx',
        'rep_president': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/prpresdistrict.aspx',
        'dem_USrepresentative': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/pdusrep.aspx',
        'rep_USrepresentative': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/prusrep.aspx',
        'dem_state_senate': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/pdohsen.aspx',
        'rep_state_senate': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/prohsen.aspx',
        'dem_state_representative': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/pdohrep.aspx',
        'rep_state_representative': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2008ElectionResults/prohrep.aspx'
        }

def make_state_representative_df():
    representative_df = pd.DataFrame()
    df = pd.read_html(URLS['dem_state_representative'])[0]
    df.columns = ['county',
                  'candidate1', 'candidate2', 'candidate3', 'candidate4', 'candidate5']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('DISTRICT')].index.tolist()
    splits.append(df.shape[0])

    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        df_.columns = ['county', 'candidate', 'votes']
        df_ = df_[df_['county'] != '']


        df_['party'] = 'Democratic'
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['office'] = 'State Representative'
        representative_df = representative_df.append(df_)

    df = pd.read_html(URLS['rep_state_representative'])[0]
    df.columns = ['county',
                  'candidate1', 'candidate2', 'candidate3', 'candidate4', 'candidate5']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('DISTRICT')].index.tolist()
    splits.append(df.shape[0])

    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        df_.columns = ['county', 'candidate', 'votes']
        df_ = df_[df_['county'] != '']


        df_['party'] = 'Republican'
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['office'] = 'State Representative'
        representative_df = representative_df.append(df_)

    return representative_df

def make_USrepresentative_df():
    representative_df = pd.DataFrame()

    df = pd.read_html(URLS['dem_USrepresentative'])[0]
    df.columns = ['county', 'candidate1', 'candidate2',
                  'candidate3', 'candidate4', 'candidate5', 'candidate6']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('DISTRICT')].index.tolist()
    splits.append(df.shape[0])
    
    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        df_.columns = ['county', 'candidate', 'votes']
        df_ = df_[df_['county'] != '']


        df_['party'] = 'Democratic'
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['office'] = 'US Representative'
        representative_df = representative_df.append(df_)

    df = pd.read_html(URLS['rep_USrepresentative'])[0]
    df.columns = ['county', 'candidate1', 'candidate2',
                  'candidate3', 'candidate4', 'candidate5']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('DISTRICT')].index.tolist()
    splits.append(df.shape[0])
    
    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        df_.columns = ['county', 'candidate', 'votes']
        df_ = df_[df_['county'] != '']


        df_['party'] = 'Republican'
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['office'] = 'US Representative'
        representative_df = representative_df.append(df_)

    return representative_df

def make_state_senate_df():
    representative_df = pd.DataFrame()
    df = pd.read_html(URLS['dem_state_senate'])[0]
    df.columns = ['county',
                  'candidate1', 'candidate2']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('DISTRICT')].index.tolist()
    splits.append(df.shape[0])
    
    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        df_.columns = ['county', 'candidate', 'votes']
        df_ = df_[df_['county'] != '']

        df_['party'] = 'Democratic'
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['office'] = 'State Senate'
        representative_df = representative_df.append(df_)

    df = pd.read_html(URLS['rep_state_senate'])[0]
    df.columns = ['county',
                  'candidate1', 'candidate2', 'candidate3']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('DISTRICT')].index.tolist()
    splits.append(df.shape[0])
    
    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        df_.columns = ['county', 'candidate', 'votes']
        df_ = df_[df_['county'] != '']

        df_['party'] = 'Republican'
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['office'] = 'State Senate'
        representative_df = representative_df.append(df_)

    return representative_df


def make_president_df():
    representative_df = pd.DataFrame()
    df = pd.read_html(URLS['dem_president'])[0]
    df.columns = ['county',
                  'candidate1', 'candidate2', 'candidate3']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('DISTRICT')].index.tolist()
    splits.append(df.shape[0])
    
    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        df_.columns = ['county', 'candidate', 'votes']
        df_ = df_[df_['county'] != '']

        df_['party'] = 'Democratic'
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['office'] = 'President'
        representative_df = representative_df.append(df_)

    df = pd.read_html(URLS['rep_president'])[0]
    df.columns = ['county',
                  'candidate1', 'candidate2', 'candidate3', 'candidate4',
                  'candidate5']
    df['county'] = df['county'].fillna('') 
    splits = df[df.county.str.startswith('DISTRICT')].index.tolist()
    splits.append(df.shape[0])
    
    for split in range(len(splits) - 1):
        df_ = df.iloc[splits[split]:splits[split+1]]
        df_ = df_.drop(df_.index[0])
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=[df_.columns.values[1]])
        df_ = df_.dropna(axis=1)
        
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        df_.columns = ['county', 'candidate', 'votes']
        df_ = df_[df_['county'] != '']

        df_['party'] = 'Republican'
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['office'] = 'President'
        representative_df = representative_df.append(df_)

    return representative_df

def make_results():
    president_df = make_president_df()
    state_representative_df = make_state_representative_df()
    us_representative_df = make_USrepresentative_df()
    senate_df = make_state_senate_df()

    dfs = [president_df, state_representative_df,
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
results.to_csv('20080304__oh__primary.csv', index=False, encoding='latin')
