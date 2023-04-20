import pandas as pd
import numpy as np

def get_crime_data(state_name, county_name, excel_data, years, trend):
    print("Reading", state_name, county_name)
    selected_df = excel_data[-1][["State","County","Violent Crime Rate","Injury Death Rate"]]
    selected_df = selected_df.loc[(selected_df['State'] == state_name) & (selected_df['County'] == county_name)]
    del selected_df[selected_df.columns.values[0]]
    del selected_df[selected_df.columns.values[0]]
    print(selected_df)
    return selected_df

# get_regulated_industries_data("California","Alameda")