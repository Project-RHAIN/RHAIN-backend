import pandas as pd

def getClinicalData(state_name, county_name):
    # Read the Excel file into a pandas dataframe
    df = pd.read_excel('app/data/Clinical_Care_CA.xlsx')    

    # Filter the rows by county
    county_df = df.loc[df['County'] == county_name]

    # Select the columns you want
    selected_columns = ['Primary Care Physicians Ratio Formatted', 'Dentist Ratio Formatted', 'Mental Health Provider Ratio Formatted']
    selected_df = county_df[selected_columns]

    # Print the selected data
    return selected_df
    # print(selected_df)