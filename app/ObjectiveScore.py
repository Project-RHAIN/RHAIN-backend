import pandas as pd
import openpyxl
import os

data_path_cumulative_score = os.path.join(os.getcwd(), 'app/data/cumulative_score.xlsx')
cumulative_data = pd.read_excel(data_path_cumulative_score)

data_path_feature_score = os.path.join(os.getcwd(), 'app/data/feature_wise_score.xlsx')
feature_data = pd.read_excel(data_path_feature_score)

data_path_compare_score = os.path.join(os.getcwd(), 'app/data/compare_counties_scores.xlsx')
compare_data = pd.read_excel(data_path_compare_score)

def getOverallObjectiveScore(state, county):
    # Ruled Based is based on Statistical Analysis performed over Static data
    # The Data points have been passed through the System and scores have been calculated and stored in excel
    # This function fetches the scores and returns them based on User Input    
    state_data = cumulative_data.loc[cumulative_data["State"] == state]
    county_data = state_data.loc[state_data["County"] == county]
    rel_val = None
    for dx,d in county_data.iterrows():
         rel_val = round(d["Health Score"],2)
    return {"Health Score":rel_val}


def getFeatureScore(state, county, feature_name):
    # Ruled Based is based on Statistical Analysis performed over Static data
    # The Data points have been passed through the System and scores have been calculated and stored in excel
    # This function fetches the scores and returns them based on User Input
    state_data = feature_data.loc[feature_data["State"] == state]
    county_data = state_data.loc[state_data["County"] == county]
    feature_specific = county_data.loc[county_data["Feature Name"]==feature_name]
    rel_val = None
    for dx,d in feature_specific.iterrows():
         rel_val = round(d["Zscore"]/10,2)
    return {feature_name: rel_val}

def getCompareScore(state, county, feature_name):
    # Ruled Based is based on Statistical Analysis performed over Static data
    # The Data points have been passed through the System and scores have been calculated and stored in excel
    # This function fetches the scores and returns them based on User Input
    state_data = compare_data.loc[compare_data["State"] == state]
    county_data = state_data.loc[state_data["County"] == county]
    feature_specific = county_data.loc[county_data["Feature Name"]==feature_name]
    rel_val = None
    for dx,d in feature_specific.iterrows():
         rel_val = round(d["Feature Value"]/10,2)
    return {feature_name: rel_val}

