import pandas as pd
import os


def getOverallObjectiveScore(state, county):
    # Ruled Based is based on Statistical Analysis performed over Static data
    # The Data points have been passed through the System and scores have been calculated and stored in excel
    # This function fetches the scores and returns them based on User Input
    data_path = os.path.join(os.getcwd(), 'app/data/cumulative_score.xlsx')
    all_data = pd.read_excel(data_path)
    state_data = all_data.loc[all_data["State"] == state]
    county_data = state_data.loc[state_data["County"] == county]
    rel_val = None
    for dx,d in county_data.iterrows():
         rel_val = round(d["Health Score"],2)
    return {"Health Score":rel_val}


def getFeatureScore(state, county, feature_name):
    # Ruled Based is based on Statistical Analysis performed over Static data
    # The Data points have been passed through the System and scores have been calculated and stored in excel
    # This function fetches the scores and returns them based on User Input
    data_path = os.path.join(os.getcwd(), 'app/data/feature_wise_score.xlsx')
    all_data = pd.read_excel(data_path)
    state_data = all_data.loc[all_data["State"] == state]
    county_data = state_data.loc[state_data["County"] == county]
    feature_specific = county_data.loc[county_data["Feature Name"]==feature_name]
    rel_val = None
    for dx,d in feature_specific.iterrows():
         rel_val = round(d["Zscore"],2)
    return {"Feature Score":rel_val}


# getOverallObjectiveScore("California", "Marin", "% Fair or Poor Health")