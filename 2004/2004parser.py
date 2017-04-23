import pandas as pd

URLS = {'President': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2004ElectionsResults/04-1102PresVicePres.aspx',
        'US Senate': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2004ElectionsResults/04-1102USSenator.aspx',
        'US Representatives': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2004ElectionsResults/04-1102USReps.aspx',
        'State Senate': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2004ElectionsResults/04-1102OHSenate.aspx',
        'State House': 'https://www.sos.state.oh.us/sos/elections/Research/electResultsMain/2004ElectionsResults/04-1102OHReps.aspx'
        }

COLS = ['county', 'candidate', 'party', 'office', 'district', 'votes', 'pct']


def make_president_df():
    df = pd.read_html(URLS['President'])[0]
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.dropna(subset=['COUNTY'])

    df.columns = ['county'] + list(df.columns[1:])
    df_ = pd.melt(df, id_vars=['county'], value_vars=list(df.columns[1:]))
    df_.columns = ['county', 'candidate', 'votes']
    df_['district'] = ''
    df_['candidate'] = df_['candidate'].str.lstrip('*')
    df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
    df_['candidate'] = df_['candidate'].str.rstrip('()')
    df_['party'] = 'Non-Partisan'
    df_.loc[df_['candidate'] == 'George W. Bush', 'party'] = 'Republican'
    df_.loc[df_['candidate'] == 'John F. Kerry', 'party'] = 'Democratic'
    df_['office'] = 'President'
    df_ = df_[df_['county'] != 'Total'][df_['county'] != 'Percentage of Votes']
    president_df = df_
    return president_df


def make_USsenate_df():
    df = pd.read_html(URLS['US Senate'])[0]
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.dropna(subset=['COUNTY'])

    df.columns = ['county'] + list(df.columns[1:])
    df_ = pd.melt(df, id_vars=['county'], value_vars=list(df.columns[1:]))
    df_.columns = ['county', 'candidate', 'votes']
    df_['district'] = ''
    df_['candidate'] = df_['candidate'].str.lstrip('*')
    df_['candidate'] = df_['candidate'].str.replace('\((.*?)\)', '')
    df_['candidate'] = df_['candidate'].str.rstrip('()')
    df_['party'] = 'Non-Partisan'
    df_.loc[df_['candidate'] == 'George V. Voinovich', 'party'] = 'Republican'
    df_.loc[df_['candidate'] == 'Eric D. Fingerhut', 'party'] = 'Democratic'
    df_['office'] = 'US Senate'
    df_ = df_[df_['county'] != 'Total'][df_['county'] != 'Percentage of Votes']
    senate_df = df_
    return senate_df


def make_USrepresentative_df():
    df = pd.read_html(URLS['US Representatives'])[0]
    df['district'] = df[0].str.extract('DISTRICT NUMBER:(.*)$').str[-2:]
    df['district'] = df['district'].ffill()
    rep_df = pd.DataFrame()
    for district in df['district'].unique():
        df_ = df[df['district'] == district]
        col1 = df_.iloc[[1, 2]][1].str.cat(sep=' ')
        col2 = df_.iloc[[1, 2]][2].str.cat(sep=' ')
        col3 = df_.iloc[[1, 2]][3].str.cat(sep=' ')
        df_.columns = ['county', col1, col2, col3, 'district']
        df_.drop(df_.index[:3], inplace=True)
        df_ = df_.dropna(subset=['county', df_.columns[1]])
        df_ = df_.drop('district', 1)
        df_ = pd.melt(df_, id_vars=['county'],
                      value_vars=list(df_.columns[1:]))
        df_['district'] = district
        df_.columns = ['county', 'candidate', 'votes', 'district']
        df_['county'] = df_['county'].str.rstrip(' **')
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_["party"] = df_["candidate"].str.split().str[-1]
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_ = df_.dropna(subset=['candidate'])
        df_['candidate'] = df_["candidate"].str.split(
        ).str[:-1].apply(lambda x: ' '.join(x))
        df_['candidate'] = df_['candidate'].str.rstrip(' (WI)')
        df_ = df_[df_['county'] != 'Total'][df_['county'] != 'Percentage of Votes']
        df_['office'] = 'US Representatives'
        rep_df = rep_df.append(df_)
    return rep_df

def make_statesenate_df():
    df = pd.read_html(URLS['State Senate'])[0]
    df['district'] = df[0].str.extract('DISTRICT NUMBER:(.*)$').str[-2:]
    df['district'] = df['district'].ffill()
    staterep_df = pd.DataFrame()
    for district in df['district'].unique():
        df_ = df[df['district'] == district]
        col1 = df_.iloc[[1, 2]][1].str.cat(sep=' ')
        col2 = df_.iloc[[1, 2]][2].str.cat(sep=' ')
        col3 = df_.iloc[[1, 2]][3].str.cat(sep=' ')
        df_.columns = ['county', col1, col2, col3, 'district']
        df_.drop(df_.index[:3], inplace=True)
        df_ = df_.dropna(subset=['county', df_.columns[1]])
        df_ = df_.drop('district', 1)
        df_ = pd.melt(df_, id_vars=['county'],
                      value_vars=list(df_.columns[1:]))
        df_['district'] = district
        df_.columns = ['county', 'candidate', 'votes', 'district']
        df_['county'] = df_['county'].str.rstrip(' **')
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_["party"] = df_["candidate"].str.split().str[-1]
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_ = df_.dropna(subset=['candidate'])
        df_['candidate'] = df_["candidate"].str.split(
        ).str[:-1].apply(lambda x: ' '.join(x))
        df_['candidate'] = df_['candidate'].str.rstrip(' (WI)')
        df_ = df_[df_['county'] != 'Total'][df_['county'] != 'Percentage of Votes']
        df_['office'] = 'State Senate'
        staterep_df = staterep_df.append(df_)
    return staterep_df

def make_statehouse_df():
    df = pd.read_html(URLS['State House'])[0]
    df['district'] = df[0].str.extract('DISTRICT NUMBER:(.*)$').str[-2:]
    df['district'] = df['district'].ffill()
    staterep_df = pd.DataFrame()
    for district in df['district'].unique():
        df_ = df[df['district'] == district]
        col1 = df_.iloc[[1, 2]][1].str.cat(sep=' ')
        col2 = df_.iloc[[1, 2]][2].str.cat(sep=' ')
        col3 = df_.iloc[[1, 2]][3].str.cat(sep=' ')
        col4 = df_.iloc[[1, 2]][4].str.cat(sep=' ')
        df_.columns = ['county', col1, col2, col3, col4, 'district']
        df_.drop(df_.index[:3], inplace=True)
        df_ = df_.dropna(subset=['county', df_.columns[1]])
        df_ = df_.drop('district', 1)
        df_ = pd.melt(df_, id_vars=['county'], value_vars=list(df_.columns[1:]))
        df_['district'] = district
        df_.columns = ['county', 'candidate', 'votes', 'district']
        df_['county'] = df_['county'].str.rstrip(' **')
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_["party"] = df_["candidate"].str.split().str[-1]
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_ = df_.dropna(subset=['candidate'])
        df_['candidate'] = df_["candidate"].str.split(
        ).str[:-1].apply(lambda x: ' '.join(x))
        df_['candidate'] = df_['candidate'].str.rstrip(' (WI)')
        df_ = df_[df_['county'] != 'Total'][df_['county'] != 'Percentage of Votes']
        df_['office'] = 'State House'
        staterep_df = staterep_df.append(df_)
    return staterep_df



def make_results():
    president_df = make_president_df()
    senate_df = make_USsenate_df()
    rep_df = make_USrepresentative_df()
    staterep_df = make_statehouse_df()
    statesenate_df = make_statesenate_df()

    dfs = [president_df, senate_df, rep_df,
           staterep_df, statesenate_df]

    results = pd.DataFrame()
    for df in dfs:
        results = results.append(df)
    results = results[~results['county'].str.contains('Total')]
    results = results[~results['county'].str.contains('Percentage')]
    return results

results = make_results()
results.to_csv('20040302__oh__primary.csv', index=False, encoding='latin')
