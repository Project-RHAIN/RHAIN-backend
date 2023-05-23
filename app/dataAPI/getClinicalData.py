import pandas as pd
import numpy as np

def convertRatio (x):
    if x is np.nan:
        return np.nan
    a, b = x.split(':')
    if int(b) == 0:
        return int(a) 
    c = int(a)/int(b) 
    return c

def getClinicalData(state_name, county_name, excel_data, years, trend):
    print("Reading", state_name, county_name)
    # Read the Excel file into a pandas dataframe    
    # print("p1")
    if not trend:
        selected_df = excel_data[-1][["State","County","Primary Care Physicians Ratio","Dentist Ratio","Mental Health Provider Ratio"]]    
        selected_df = selected_df.loc[(selected_df['State'] == state_name) & (selected_df['County'] == county_name)]
        del selected_df[selected_df.columns.values[0]]
        del selected_df[selected_df.columns.values[0]]     
        for col in ["Primary Care Physicians Ratio","Dentist Ratio","Mental Health Provider Ratio"]:
            selected_df[col] = selected_df[col].apply(convertRatio)
        print("Done")
        return selected_df

    dfs = []
    for i in range(len(excel_data)):
        # print(i)
        selected_df_multiple = excel_data[i][["State","County","Primary Care Physicians Ratio","Dentist Ratio","Mental Health Provider Ratio"]]
        selected_df_multiple = selected_df_multiple.loc[(selected_df_multiple['State'] == state_name) & (selected_df_multiple['County'] == county_name)]
        del selected_df_multiple[selected_df_multiple.columns.values[0]]
        del selected_df_multiple[selected_df_multiple.columns.values[0]]
        for col in ["Primary Care Physicians Ratio","Dentist Ratio","Mental Health Provider Ratio"]:
            selected_df_multiple[col] = selected_df_multiple[col].apply(convertRatio)
        selected_df_multiple.insert(0,"Year",int(years[i]))
        dfs.append(selected_df_multiple)
    
    return pd.concat(dfs)

