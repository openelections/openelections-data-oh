import pandas as pd

GENERAL_URLS = {'Governor/LtGovernor': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/governor-and-lieutenant-governor-november-7-2006/',
                'Attorney General': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/attorney-general-november-7-2006/',
                'State Auditor': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/auditor-of-state-november-7-2006/',
                'Secretary of State': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/secretary-of-state-november-7-2006/',
                'State Treasure': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/treasurer-of-state-november-7-2006/',
                'State Senate': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/ohio-senate-november-7-2006/',
                'US Senate': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/u.s.-senate-november-7-2006/',
                'US House of Representatives': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/u.s.-house-of-representatives-november-7-2006/',
                'State Representative': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/ohio-house-of-representatives-november-7-2006/'
                }

DEMOCRATIC_PRIMARY_URLS = {'Governor/LtGovernor': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/democratic-governor--lieutenant-governor-may-2-2006/',
                           'Attorney General': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/democratic-attorney-general-may-2-2006/',
                           'State Auditor': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/democratic-auditor-of-state-may-2-2006/',
                           'Secretary of State': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/democratic-secretary-of-state-may-2-2006/',
                           'State Senate': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/democratic-ohio-senate-may-2-2006/',
                           'State Treasure': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/democratic-treasurer-of-state-may-2-2006/',
                           'US Senate': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/democratic-u.s.-senate-may-2-2006/',
                           'US House of Representatives': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/democratic-u.s.-house-of-representatives-may-2-2006/',
                           'State Senate': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/democratic-ohio-senate-may-2-2006/',
                           'State Representative': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/democratic-ohio-house-of-representatives-may-2-2006/'
                           }

REPUBLICAN_PRIMARY_URLS = {'Governor/LtGovernor': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-governor--lieutenant-governor-may-2-2006/',
                           'Attorney General': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-attorney-general-may-2-2006/',
                           'State Auditor': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-auditor-of-state-may-2-2006/',
                           'Secretary of State': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-secretary-of-state-may-2-2006/',
                           'State Treasure': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-treasurer-of-state-may-2-2006/',
                           'US Senate': "https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-u.s.-senate-may-2-2006/",
                           'US House of Representatives': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-u.s.-house-of-representatives-may-2-2006/',
                           'State Senate': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-ohio-senate-may-2-2006/',
                           'State Representative': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-ohio-house-of-representatives-may-2-2006/'
                           }

COLS = ['county', 'candidate', 'party', 'office', 'district', 'votes']


def make_governor_df(url_dict, party):
    df = pd.read_html(url_dict['Governor/LtGovernor'])[0]
    df.columns = df.iloc[0].str.rstrip(' (WI)').str.lstrip('*')
    df = df.dropna(subset=['COUNTY'])
    df = df.iloc[1:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'GOVERNOR/LIEUTENANT GOVERNOR'
    df['party'] = party
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    df['candidate'] = df.candidate.str.lstrip('*')
    return df


def make_attorney_general_df(url_dict, party):
    df = pd.read_html(url_dict['Attorney General'])[0]
    df.columns = df.iloc[0]
    df = df.dropna(subset=['COUNTY'])
    df = df.iloc[1:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'ATTORNEY GENERAL'
    df['party'] = party
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    df['candidate'] = df.candidate.str.lstrip('*')
    return df


def make_state_auditor_df(url_dict, party):
    df = pd.read_html(url_dict['State Auditor'])[0]
    df.columns = df.iloc[0]
    df = df.dropna(subset=['COUNTY'])
    df = df.iloc[5:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'STATE AUDITOR'
    df['party'] = party
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    df['candidate'] = df.candidate.str.lstrip('*')
    return df


def make_secretary_of_state_df(url_dict, party):
    df = pd.read_html(url_dict['Secretary of State'])[0]
    df.columns = df.iloc[0]
    df = df.dropna(subset=['COUNTY'])
    df = df.iloc[1:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'SECRETARY OF STATE'
    df['party'] = party
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    df['candidate'] = df.candidate.str.lstrip('*')
    return df


def make_state_treasure_df(url_dict, party):
    df = pd.read_html(url_dict['State Treasure'])[0]
    df.columns = df.iloc[0]
    df = df.dropna(subset=['COUNTY'])
    df = df.iloc[1:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'STATE TREASURE'
    df['party'] = party
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    df['candidate'] = df.candidate.str.lstrip('*')
    return df


def make_us_senate_df(url_dict, party):
    df = pd.read_html(url_dict['US Senate'])[0]
    df.columns = df.iloc[0]
    df = df.dropna(subset=['COUNTY'])
    party_df.columns = ['Candidate', 'Party']
    df = df.iloc[1:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'US SENATE'
    df['party'] = party
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    df['candidate'] = df.candidate.str.lstrip('*')
    return df


def make_us_house_of_reps_df(url_dict, party):
    df = pd.read_html(url_dict['US House of Representatives'])[0]
    df['district'] = df[0].str.extract('DISTRICT NUMBER:(.*)$').str[-2:]
    df['district'] = df['district'].ffill()
    df = df.dropna(subset=['district'])
    rep_df = pd.DataFrame()
    for district in df['district'].unique():
        df_ = df[df['district'] == district]
        df_ = df_.drop('district', 1)
        df_.columns = df_.iloc[1]
        df_ = df_.iloc[2:]
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=['county', df_.columns[1]])
        df_ = pd.melt(df_, id_vars=['county'],
                      value_vars=list(df_.columns[1:]))
        df_['district'] = district
        df_.columns = ['county', 'candidate', 'votes', 'district']
        df_ = df_.dropna(subset=['votes'])
        df_['county'] = df_['county'].str.rstrip(' **')
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_["party"] = party
        df_ = df_.dropna(subset=['candidate'])
        df_ = df_[df_['county'] != 'Total'][df_['county'] != 'Percentage of Votes']
        df_['office'] = 'US REPRESENTATIVES'
        rep_df = rep_df.append(df_)
    rep_df['candidate'] = rep_df.candidate.str.lstrip('*')
    return rep_df


def make_state_representatives_df(url_dict, party):
    df = pd.read_html(url_dict['State Representative'])[0]
    df['district'] = df[0].str.extract('DISTRICT NUMBER:(.*)$').str[-2:]
    df['district'] = df['district'].ffill()
    df = df.dropna(subset=['district'])
    rep_df = pd.DataFrame()
    for district in df['district'].unique():
        df_ = df[df['district'] == district]
        df_ = df_.drop('district', 1)
        df_.columns = df_.iloc[1]
        df_ = df_.iloc[2:]
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=['county', df_.columns[1]])
        df_ = pd.melt(df_, id_vars=['county'],
                      value_vars=list(df_.columns[1:]))
        df_['district'] = district
        df_.columns = ['county', 'candidate', 'votes', 'district']
        df_ = df_.dropna(subset=['votes'])
        df_['county'] = df_['county'].str.rstrip(' **')
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_["party"] = party
        df_ = df_.dropna(subset=['candidate'])
        df_ = df_[df_['county'] != 'Total'][df_['county'] != 'Percentage of Votes']
        df_['office'] = 'STATE REPRESENTATIVES'
        rep_df = rep_df.append(df_)
    rep_df['candidate'] = rep_df.candidate.str.lstrip('*')
    return rep_df


def make_state_senate_df(url_dict, party):
    df = pd.read_html(url_dict['State Senate'])[0]
    df['district'] = df[0].str.extract('DISTRICT NUMBER:(.*)$').str[-2:]
    df['district'] = df['district'].ffill()
    df = df.dropna(subset=['district'])
    rep_df = pd.DataFrame()
    for district in df['district'].unique():
        df_ = df[df['district'] == district]
        df_ = df_.drop('district', 1)
        df_.columns = df_.iloc[1]
        df_ = df_.iloc[2:]
        df_.columns = ['county'] + list(df_.columns[1:])
        df_ = df_.dropna(subset=['county', df_.columns[1]])
        df_ = pd.melt(df_, id_vars=['county'],
                      value_vars=list(df_.columns[1:]))
        df_['district'] = district
        df_.columns = ['county', 'candidate', 'votes', 'district']
        df_ = df_.dropna(subset=['votes'])
        df_['county'] = df_['county'].str.rstrip(' **')
        df_['candidate'] = df_['candidate'].str.lstrip('*')
        df_["party"] = party
        df_ = df_.dropna(subset=['candidate'])
        df_ = df_[df_['county'] != 'Total'][df_['county'] != 'Percentage of Votes']
        df_['office'] = 'STATE SENATE'
        rep_df = rep_df.append(df_)
    rep_df['candidate'] = rep_df.candidate.str.lstrip('*')
    return rep_df

def make_primary_df():
    dfs = []
    dfs.append(make_governor_df(DEMOCRATIC_PRIMARY_URLS, 'Democratic'))
    dfs.append(make_attorney_general_df(DEMOCRATIC_PRIMARY_URLS, 'Democratic'))
    dfs.append(make_secretary_of_state_df(DEMOCRATIC_PRIMARY_URLS, 'Democratic'))
    dfs.append(make_state_auditor_df(DEMOCRATIC_PRIMARY_URLS, 'Democratic'))
    dfs.append(make_state_representatives_df(DEMOCRATIC_PRIMARY_URLS, 'Democratic'))
    dfs.append(make_state_senate_df(DEMOCRATIC_PRIMARY_URLS, 'Democratic'))
    dfs.append(make_state_treasure_df(DEMOCRATIC_PRIMARY_URLS, 'Democratic'))
    dfs.append(make_us_house_of_reps_df(DEMOCRATIC_PRIMARY_URLS, 'Democratic'))
    dfs.append(make_us_senate_df(DEMOCRATIC_PRIMARY_URLS, 'Democratic'))
    
    dfs.append(make_governor_df(REPUBLICAN_PRIMARY_URLS, 'Republican'))
    dfs.append(make_attorney_general_df(REPUBLICAN_PRIMARY_URLS, 'Republican'))
    dfs.append(make_secretary_of_state_df(REPUBLICAN_PRIMARY_URLS, 'Republican'))
    dfs.append(make_state_auditor_df(REPUBLICAN_PRIMARY_URLS, 'Republican'))
    dfs.append(make_state_representatives_df(REPUBLICAN_PRIMARY_URLS, 'Republican'))
    dfs.append(make_state_senate_df(REPUBLICAN_PRIMARY_URLS, 'Republican'))
    dfs.append(make_state_treasure_df(REPUBLICAN_PRIMARY_URLS, 'Republican'))
    dfs.append(make_us_house_of_reps_df(REPUBLICAN_PRIMARY_URLS, 'Republican'))
    dfs.append(make_us_senate_df(REPUBLICAN_PRIMARY_URLS, 'Republican'))

    df = pd.concat(dfs)
    return df


if __name__  == '__main__':
    df = make_primary_df()
    df.to_csv('20060502__OH__primary.csv', index=False)
    
