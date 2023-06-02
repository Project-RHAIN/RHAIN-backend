import pandas as pd
import numpy as np
import os

def convertRatio (x):
    if x is np.nan:
        return np.nan
    a, b = x.split(':')
    if int(b) == 0:
        return int(a) 
    c = int(a)/int(b) 
    return c

def getMapVisData(state_name, mapVis, excel_data):
    selected_df = excel_data[-1][["State","County",mapVis]]        
    selected_df = selected_df.loc[(selected_df['State'] == state_name)].tail(-1)
    del selected_df[selected_df.columns.values[0]]
    selected_df = selected_df.rename(columns={mapVis: 'values'})
    # print(selected_df)
    if mapVis in ["Primary Care Physicians Ratio","Dentist Ratio","Mental Health Provider Ratio"]:
        selected_df['values'] = selected_df['values'].apply(convertRatio)
    # for col in ["Primary Care Physicians Ratio","Dentist Ratio","Mental Health Provider Ratio"]:
    #     selected_df[col] = selected_df[col].apply(convertRatio)
    # print("Done")
    return selected_df