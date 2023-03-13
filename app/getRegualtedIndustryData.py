import pandas as pd

def get_regulated_industries_data(state_name, county_name, excel_data, years):
    print("Reading", state_name, county_name)
    selected_df = excel_data[-1][["State","County","% Smokers","% Excessive Drinking","% Driving Deaths with Alcohol Involvement"]]
    selected_df = selected_df.loc[(selected_df['State'] == state_name) & (selected_df['County'] == county_name)]
    del selected_df[selected_df.columns.values[0]]
    del selected_df[selected_df.columns.values[0]]
    print(selected_df)
    return selected_df
