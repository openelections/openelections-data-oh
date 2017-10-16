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
                           'State Auditor': 'https://www.sos.,state.oh.us/elections/election-results-and-data/2006-elections-results/republican-auditor-of-state-may-2-2006/',
                           'Secretary of State': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-secretary-of-state-may-2-2006/',
                           'State Treasure': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-treasurer-of-state-may-2-2006/',
                           'US Senate': "https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-u.s.-senate-may-2-2006/",
                           'US House of Representatives': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-u.s.-house-of-representatives-may-2-2006/',
                           'State Senate': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-ohio-senate-may-2-2006/',
                           'State Representative': 'https://www.sos.state.oh.us/elections/election-results-and-data/2006-elections-results/republican-ohio-house-of-representatives-may-2-2006/'
                           }

COLS = ['county', 'candidate', 'party', 'office', 'district', 'votes']


def make_governor_df():
    df = pd.read_html(GENERAL_URLS['Governor/LtGovernor'])[0]
    df.columns = df.iloc[0].str.rstrip(' (WI)').str.lstrip('*')
    df['COUNTY'].iloc[1]='Party'
    df = df.dropna(subset=['COUNTY'])
    party_df = df.iloc[1]
    party_df.columns = ['Candidate', 'Party']
    df = df.iloc[2:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'GOVERNOR/LIEUTENANT GOVERNOR'
    df['party'] = df.candidate.map(party_df)
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    return df


def make_attorney_general_df():
    df = pd.read_html(GENERAL_URLS['Attorney General'])[0]
    df.columns = df.iloc[3].str.rstrip(' (WI)').str.lstrip('*')
    df['COUNTY'].iloc[4]='Party'
    df = df.dropna(subset=['COUNTY'])
    party_df = df.iloc[3]
    party_df.columns = ['Candidate', 'Party']
    df = df.iloc[5:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'ATTORNEY GENERAL'
    df['party'] = df.candidate.map(party_df)
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    return df


def make_state_auditor_df():
    df = pd.read_html(GENERAL_URLS['State Auditor'])[0]
    df.columns = df.iloc[3].str.rstrip(' (WI)').str.lstrip('*')
    df['COUNTY'].iloc[4]='Party'
    df = df.dropna(subset=['COUNTY'])
    party_df = df.iloc[3]
    party_df.columns = ['Candidate', 'Party']
    df = df.iloc[5:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'STATE AUDITOR'
    df['party'] = df.candidate.map(party_df)
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    return df


def make_secretary_of_state_df():
    df = pd.read_html(GENERAL_URLS['Secretary of State'])[0]
    df.columns = df.iloc[3].str.rstrip(' (WI)').str.lstrip('*')
    df['COUNTY'].iloc[4]='Party'
    df = df.dropna(subset=['COUNTY'])
    party_df = df.iloc[3]
    party_df.columns = ['Candidate', 'Party']
    df = df.iloc[5:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'SECRETARY OF STATE'
    df['party'] = df.candidate.map(party_df)
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    return df


def make_state_treasure_df():
    df = pd.read_html(GENERAL_URLS['State Treasure'])[0]
    df.columns = df.iloc[3].str.rstrip(' (WI)').str.lstrip('*')
    df['COUNTY'].iloc[4]='Party'
    df = df.dropna(subset=['COUNTY'])
    party_df = df.iloc[3]
    party_df.columns = ['Candidate', 'Party']
    df = df.iloc[5:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'STATE TREASURE'
    df['party'] = df.candidate.map(party_df)
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    return df


def make_us_senate_df():
    df = pd.read_html(GENERAL_URLS['US Senate'])[0]
    df.columns = df.iloc[3].str.rstrip(' (WI)').str.lstrip('*')
    df['COUNTY'].iloc[4]='Party'
    df = df.dropna(subset=['COUNTY'])
    party_df = df.iloc[3]
    party_df.columns = ['Candidate', 'Party']
    df = df.iloc[5:]
    df = (pd.melt(df, id_vars=['COUNTY'], value_vars=list(df.columns[1:])))
    df.columns = ['county', 'candidate', 'votes']
    df['office'] = 'US SENATE'
    df['party'] = df.candidate.map(party_df)
    df = df[~df.county.str.startswith('Percentage')]
    df = df[~df.county.str.startswith('Total')]
    return df


def make_us_house_of_reps_df():
    pass


def make_state_representatives_df():
    pass


def make_state_senate_df():
    pass
