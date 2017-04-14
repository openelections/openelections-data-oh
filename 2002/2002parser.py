import pandas as pd

URLS = {'Governor': 'http://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2002Results/gov.aspx',
        'Attorney General/Auditor': 'http://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2002Results/attyaud.aspx',
        'Secretary/Treasure': 'http://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2002Results/sostreas.aspx',
        'State Senate': 'http://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2002Results/ohsen.aspx',
        'State Representative': 'http://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2002Results/ohrep.aspx',
        'US Representative': 'http://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2002Results/usrep.aspx'
        }

COLS = ['county', 'candidate', 'party', 'office', 'district', 'votes', 'pct']


def make_governor_df():
    df = pd.read_html(URLS['Governor'])[0]
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.dropna(subset=['County'])

    df.columns = ['county'] + list(df.columns[1:])
    df_ = pd.melt(df, id_vars=['county'], value_vars=list(df.columns[1:]))
    df_.columns = ['county', 'candidate', 'votes']
    df_['district'] = ''
    df_['candidate'] = df_['candidate'].str.lstrip('* ')
    df_['party'] = df_['candidate'].str.extract('\((.*?)\)')
    df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
    df_['candidate'] = df_['candidate'].str.rstrip('()')
    df_['party'].fillna('', inplace=True)
    df_['office'] = 'Governor'
    governor_df = df_

    return governor_df

df = make_governor_df()


def make_attorney_auditor_df():
    df = pd.read_html(URLS['Attorney General/Auditor'])[0]
    df = df.drop(0)
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.dropna(subset=['County'])

    df.columns = ['county'] + list(df.columns[1:])
    df_ = pd.melt(df, id_vars=['county'], value_vars=list(df.columns[[1, 2]]))
    df_.columns = ['county', 'candidate', 'votes']
    df_['district'] = ''
    df_['candidate'] = df_['candidate'].str.lstrip('* ')
    df_['party'] = df_['candidate'].str.extract('\((.*?)\)')
    df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
    df_['candidate'] = df_['candidate'].str.rstrip('()')
    df_['party'].fillna('', inplace=True)
    df_['office'] = 'Attorney General'
    attorney_df = df_

    df_ = pd.melt(df, id_vars=['county'], value_vars=list(df.columns[[3, 4]]))
    df_.columns = ['county', 'candidate', 'votes']
    df_['district'] = ''
    df_['candidate'] = df_['candidate'].str.lstrip('* ')
    df_['party'] = df_['candidate'].str.extract('\((.*?)\)')
    df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
    df_['candidate'] = df_['candidate'].str.rstrip('()')
    df_['party'].fillna('', inplace=True)
    df_['office'] = 'Auditor of State'
    auditor_df = df_

    return attorney_df, auditor_df


def make_secretary_treasure_df():
    df = pd.read_html(URLS['Secretary/Treasure'])[0]
    df = df.drop(0)
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.dropna(subset=['County'])

    df.columns = ['county'] + list(df.columns[1:])
    df_ = pd.melt(df, id_vars=['county'], value_vars=list(df.columns[[1, 2]]))
    df_.columns = ['county', 'candidate', 'votes']
    df_['district'] = ''
    df_['candidate'] = df_['candidate'].str.lstrip('* ')
    df_['party'] = df_['candidate'].str.extract('\((.*?)\)')
    df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
    df_['candidate'] = df_['candidate'].str.rstrip('()')
    df_['party'].fillna('', inplace=True)
    df_['office'] = 'Secretary of State'
    secretary_df = df_

    df_ = pd.melt(df, id_vars=['county'],
                  value_vars=list(df.columns[[3, 4, 5]]))
    df_.columns = ['county', 'candidate', 'votes']
    df_['district'] = ''
    df_['candidate'] = df_['candidate'].str.lstrip('* ')
    df_['party'] = df_['candidate'].str.extract('\((.*?)\)')
    df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
    df_['candidate'] = df_['candidate'].str.rstrip('()')
    df_['party'].fillna('', inplace=True)
    df_['office'] = 'Treasure of State'
    treasure_df = df_

    return secretary_df, treasure_df


def make_staterepresentative_df():
    df = pd.read_html(URLS['State Representative'])[0]
    df.columns = ['district', 'county',
                  'candidate1', 'candidate2', 'candidate3']
    df['district'] = df['district'].fillna(method='ffill')
    df = df.dropna(subset=['candidate1'])
    df = df.drop(0)
    df['district'] = df['district'].str.split().str[-1]
    df.head(20)

    districts = df['district'].unique()
    representative_df = pd.DataFrame()
    for district in districts:
        df_ = df[df['district'] == district]
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['district', 'county'] + list(df_.columns[2:])
        df_ = df_.dropna(axis=1)
        df_ = pd.melt(df_, id_vars=['county'],
                      value_vars=list(df_.columns[2:]))
        df_.columns = ['county', 'candidate', 'votes']
        df_['district'] = district
        df_['candidate'] = df_['candidate'].str.lstrip('* ')
        df_['party'] = df_['candidate'].str.extract('\((.*?)\)')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['party'].fillna('', inplace=True)
        df_['office'] = 'State Representative'
        representative_df = representative_df.append(df_)

    return representative_df


def make_senate_df():
    df = pd.read_html(URLS['State Senate'])[0]
    df.columns = ['district', 'county',
                  'candidate1', 'candidate2', 'candidate3']
    df['district'] = df['district'].fillna(method='ffill')
    df = df.dropna(subset=['candidate1'])
    df = df.drop(0)
    df['district'] = df['district'].str.split().str[-1]
    df.head(20)

    districts = df['district'].unique()
    senate_df = pd.DataFrame()
    for district in districts:
        df_ = df[df['district'] == district]
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['district', 'county'] + list(df_.columns[2:])
        df_ = df_.dropna(axis=1)
        df_ = pd.melt(df_, id_vars=['county'],
                      value_vars=list(df_.columns[2:]))
        df_.columns = ['county', 'candidate', 'votes']
        df_['district'] = district
        df_['candidate'] = df_['candidate'].str.lstrip('* ')
        df_['party'] = df_['candidate'].str.extract('\((.*?)\)')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['party'].fillna('', inplace=True)
        df_['office'] = 'State Senate'
        senate_df = senate_df.append(df_)

    return senate_df


def make_USrepresentative_df():
    df = pd.read_html(URLS['US Representative'])[0]
    df.columns = ['district', 'county',
                  'candidate1', 'candidate2', 'candidate3']
    df['district'] = df['district'].fillna(method='ffill')
    df = df.dropna(subset=['candidate1'])
    df = df.drop(0)
    df['district'] = df['district'].str.split().str[-1]
    df.head(20)

    districts = df['district'].unique()
    representative_df = pd.DataFrame()
    for district in districts:
        df_ = df[df['district'] == district]
        df_.columns = df_.iloc[0]
        df_ = df_.drop(df_.index[0])
        df_.columns = ['district', 'county'] + list(df_.columns[2:])
        df_ = df_.dropna(axis=1)
        df_ = pd.melt(df_, id_vars=['county'],
                      value_vars=list(df_.columns[2:]))
        df_.columns = ['county', 'candidate', 'votes']
        df_['district'] = district
        df_['candidate'] = df_['candidate'].str.lstrip('* ')
        df_['party'] = df_['candidate'].str.extract('\((.*?)\)')
        df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
        df_['candidate'] = df_['candidate'].str.rstrip('()')
        df_['party'].fillna('', inplace=True)
        df_['office'] = 'US Representative'
        representative_df = representative_df.append(df_)

    return representative_df


def make_results():
    governor_df = make_governor_df()
    attorney_df, auditor_df = make_attorney_auditor_df()
    secretary_df, treasure_df = make_secretary_treasure_df()
    state_representative_df = make_staterepresentative_df()
    us_representative_df = make_USrepresentative_df()
    senate_df = make_senate_df()

    dfs = [governor_df, attorney_df, auditor_df, secretary_df,
           treasure_df, state_representative_df, us_representative_df,
           senate_df]

    results = pd.DataFrame()
    for df in dfs:
        results = results.append(df)
    results = results[~results['county'].str.contains('Total')]
    return results

results = make_results()
results.to_csv('20021105__oh__general.csv', index=False)
