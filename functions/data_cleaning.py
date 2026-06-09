import pandas as pd
import csv


def data_cleaning(path: str):

    print('Data cleaning started...')
    df = pd.read_csv(path, sep=',', quoting=csv.QUOTE_NONE)
    df.iloc[:, [0, -1]] = df.iloc[:, [0, -1]].apply(lambda x: x.astype(str).str.replace('"', ''))
    df.columns = df.columns.str.replace('"', '')
    df=df.dropna()
    df['breakdown']=df['breakdown'].astype(int)
    df['full_load_issues']=df['full_load_issues'].astype(int)
    df['timestamp']=pd.to_datetime(df['timestamp'])
    print('Data cleaning done!')

    
    return df