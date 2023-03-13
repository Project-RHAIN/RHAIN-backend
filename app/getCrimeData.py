import pandas as pd
import numpy as np
import os

data_path_clinical_data = os.path.join(os.getcwd(), 'app/data/2022 County Health Rankings Data.xlsx')
clinical_data_excel = pd.read_excel(data_path_clinical_data ,sheet_name = 3,header=1)

def get_crime_data(state_name, county_name):
    print("Reading", state_name, county_name)
    selected_df = clinical_data_excel[["State","County","Violent Crime Rate","Injury Death Rate"]]
    selected_df = selected_df.loc[(selected_df['State'] == state_name) & (selected_df['County'] == county_name)]
    del selected_df[selected_df.columns.values[0]]
    del selected_df[selected_df.columns.values[0]]
    print(selected_df)
    return selected_df

# get_regulated_industries_data("California","Alameda")