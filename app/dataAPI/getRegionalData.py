

def get_regional_data(state_name, county_name, excel_data):       
    selected_df = excel_data[["State","County","Population","Area in Sq. miles","Population density", "Income"]]     
    selected_df = selected_df.loc[(selected_df['State'] == state_name) & (selected_df['County'] == county_name)]
    del selected_df[selected_df.columns.values[0]]
    del selected_df[selected_df.columns.values[0]]
    print(selected_df)
    return selected_df

# path_parent = os.path.dirname(os.getcwd())
# os.chdir(path_parent)
# regional_data_excel = os.path.join(os.getcwd(), 'data\\Population_Income_Area_2022.xlsx')
# regional_data = pd.read_excel(regional_data_excel)
# get_regional_data('California','El Dasdorado',regional_data)