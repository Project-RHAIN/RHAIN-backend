import pandas as pd

def getHealthData(state_name, county_name, excel_data, years, trend):
    print("Reading", state_name, county_name)

    if not trend:

        selected_df = excel_data[-1][["State","County","% Physically Inactive","% Adults with Obesity","% With Access to Exercise Opportunities"]]
        selected_df = selected_df.loc[(selected_df['State'] == state_name) & (selected_df['County'] == county_name)]
        del selected_df[selected_df.columns.values[0]]
        del selected_df[selected_df.columns.values[0]]
        print(selected_df)
        return selected_df

    dfs = []
    for i in range(len(excel_data)):
        # print(i)
        selected_df_multiple = excel_data[i][["State","County","% Physically Inactive","% Adults with Obesity","% With Access to Exercise Opportunities"]]
        selected_df_multiple = selected_df_multiple.loc[(selected_df_multiple['State'] == state_name) & (selected_df_multiple['County'] == county_name)]
        del selected_df_multiple[selected_df_multiple.columns.values[0]]
        del selected_df_multiple[selected_df_multiple.columns.values[0]]
        selected_df_multiple.insert(0,"Year",int(years[i]))
        dfs.append(selected_df_multiple)
    
    return pd.concat(dfs)
