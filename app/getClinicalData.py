import pandas as pd
import numpy as np

def convertRatio (x):
    if x is np.nan:
        return np.nan
    a, b = x.split(':') 
    c = int(a)/int(b) 
    return c

def getClinicalData(state_name, county_name, excel_data, years):
    print("Reading", state_name, county_name)
    # Read the Excel file into a pandas dataframe    
    # print("p1")
    selected_df = excel_data[-1][["State","County","Primary Care Physicians Ratio","Dentist Ratio","Mental Health Provider Ratio"]]
    # print("p2")
    selected_df = selected_df.loc[(selected_df['State'] == state_name) & (selected_df['County'] == county_name)]
    del selected_df[selected_df.columns.values[0]]
    del selected_df[selected_df.columns.values[0]] 
    # print("p3")
    for col in ["Primary Care Physicians Ratio","Dentist Ratio","Mental Health Provider Ratio"]:
        selected_df[col] = selected_df[col].apply(convertRatio)
    print("Done")
    return selected_df

