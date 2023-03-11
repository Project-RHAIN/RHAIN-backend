import pandas as pd
import numpy as np
import os

def convertRatio (x):
    if x is np.nan:
        return np.nan
    a, b = x.split(':') 
    c = int(a)/int(b) 
    return c

def getClinicalData(state_name, county_name):

    # Read the Excel file into a pandas dataframe
    data_path = os.path.join(os.getcwd(), 'app/data/2022 County Health Rankings Data.xlsx')
    xl = pd.read_excel(data_path ,sheet_name = 3,header=1)
    selected_df = xl[["State","County","Primary Care Physicians Ratio","Dentist Ratio","Mental Health Provider Ratio"]]

    selected_df = selected_df.loc[(selected_df['State'] == state_name) & (selected_df['County'] == county_name)]
    del selected_df[selected_df.columns.values[0]]
    del selected_df[selected_df.columns.values[0]]
    
    for col in ["Primary Care Physicians Ratio","Dentist Ratio","Mental Health Provider Ratio"]:
        selected_df[col] = selected_df[col].apply(convertRatio)
    return selected_df

