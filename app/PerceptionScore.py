import tensorflow as tf
import numpy as np
from transformers import DistilBertTokenizer
import random
import pandas as pd
from random import sample
import os
import csv


data_path_reviews = os.path.join(os.getcwd(), 'app/data/BackendReviews.csv')
data_path_scores = os.path.join(os.getcwd(), 'app/data/Scores.csv')
data_path_model = os.path.join(os.getcwd(), 'app/DistilBert')

with open(data_path_scores, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    rows = {(row['State'], row['County']): row['Score'] for row in reader}

df = pd.read_csv(data_path_scores)
dbModel = tf.keras.models.load_model(data_path_model)
dbTokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")


def get_reviews(county_name):
    random.seed(10)
    county_df = df[df['County'] == county_name]
    reviews = county_df['Reviews'].tolist()
    return sample(reviews, min(len(reviews), 20))


def score_compute(reviews, model, tokenizer):
    if len(reviews) != 0:
        batch = tokenizer(reviews, max_length=128, padding=True, truncation=True, return_tensors='tf')
        outputs = model(batch)
        predictions = tf.nn.softmax(outputs['logits'], axis=-1)
        score_sum = 0
        for i in predictions:
            score_sum += (i[1] - i[0])
        score = score_sum/len(reviews)
        return float(score)
    else:
        return np.nan


# def get_sentiment_score(state_name, county_name):
#     reviews = get_reviews(county_name)
#     score = round((score_compute(reviews, dbModel, dbTokenizer) + 1) * 5, 2)
#     return {"Perception score": score}

def get_score(state_name, county_name):
    score = rows.get((state_name, county_name))
    if score != 'nan':
        return score
    else:
        return -1


def get_sentiment_score(state_name, county_name):
    score = get_score(state_name, county_name)
    if score != -1:
        return {"Perception score": score}
    else:
        return {"No reviews available for scoring"}


