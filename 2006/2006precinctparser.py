import pandas

MAIN_COLS = ['COUNTY_NAME', 'STATE_PRECINCT_CODE',
             'US_CONGRESS_DISTRICT']

MAIN_COLS_RENAME = ['county', 'precinct', 'district']

PARTIES = {'Ted Strickland': 'Democratic',
           'J. Kenneth Blackwell': 'Republican',
           'Robert Fitrakis': 'Non-partisan',
           'William S. Peirce': 'Non-partisan',
           'Marc Dann': 'Democratic',
           'Betty Montgomery': 'Republican',
           'Barbara Sykes': 'Democratic',
           'Mary Taylor': 'Republican',
           'Jennifer L. Brunner': 'Democratic',
           'John A. Eastman': 'Non-partisan',
           'Greg Hartmann': 'Republican',
           'Timothy J. Kettler': 'Non-partisan',
           }

DF = pd.read_csv('gen06statewide.csv')


def make_gov_df(df=DF):
    df_gov = df[MAIN_COLS + ['GOV_D_STRICKLAND', 'GOV_R_BLACKWELL',
                             'GOV_FITRAKIS', 'GOV_PEIRCE']]
    df_gov.columns = MAIN_COLS_RENAME + ['Ted Strickland', 'J. Kenneth Blackwell',
                      'Robert Fitrakis', 'William S. Peirce']


    df_gov = (pd.melt(df_gov, id_vars=MAIN_COLS_RENAME, value_vars=list(df_gov.columns[3:])))
    df_gov.columns = MAIN_COLS_RENAME + ['candidate', 'votes']
    df_gov = df_gov.dropna(subset=['votes'])
    df_gov['office'] = 'Governor/LtGovernor'
    return df_gov

def make_ag_df(df=DF):
    df_ag = df[MAIN_COLS + ['AG_D_DANN', 'AG_R_MONTGOMERY']]
    df_ag.columns = MAIN_COLS_RENAME + ['Marc Dann', 'Betty Montgomery']

    df_ag = (pd.melt(df_ag, id_vars=MAIN_COLS_RENAME, value_vars=list(df_ag.columns[3:])))
    df_ag.columns = MAIN_COLS_RENAME + ['candidate', 'votes']
    df_ag = df_ag.dropna(subset=['votes'])
    df_ag['office'] = 'Attorney General'
    return df_ag

def make_aud_df(df=DF):
    df_aud = df[MAIN_COLS + ['AUD_D_SYKES', 'AUD_R_TAYLOR']]
    df_aud.columns = MAIN_COLS_RENAME + ['Barbara Sykes', 'Mary Taylor']

    df_aud = (pd.melt(df_aud, id_vars=MAIN_COLS_RENAME, value_vars=list(df_aud.columns[3:])))
    df_aud.columns = MAIN_COLS_RENAME + ['candidate', 'votes']
    df_aud = df_aud.dropna(subset=['votes'])
    df_aud['office'] = 'State Auditor'
    return df_aud

def make_sos_df(df=DF):
    df_sos = df[MAIN_COLS + ['SOS_D_BRUNNER', 'SOS_R_HARTMAN', 'SOS_EASTMAN', 'SOS_KETTLER']]
    df_sos.columns = MAIN_COLS_RENAME + ['Jennifer L. Brunner',
                                         'Greg Hartman',
                                         'John A. Eastman',
                                         'Timothy J. Kettler']
    df_sos = (pd.melt(df_sos, id_vars=MAIN_COLS_RENAME, value_vars=list(df_sos.columns[3:])))
    df_sos.columns = MAIN_COLS_RENAME + ['candidate', 'votes']
    df_sos = df_sos.dropna(subset=['votes'])
    df_sos['office'] = 'Secretary of State'
    return df_sos
