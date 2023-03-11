import tensorflow as tf
import numpy as np
from transformers import DistilBertTokenizer
import random
import pandas as pd
from random import sample
import os


data_path_reviews = os.path.join(os.getcwd(), 'data\BackendReviews.csv')
data_path_model = os.path.join(os.getcwd(), 'DistilBert')

df = pd.read_csv(data_path_reviews)
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


def get_sentiment_score(state_name, county_name):
    reviews = get_reviews(county_name)
    return (score_compute(reviews, dbModel, dbTokenizer) + 1) * 5




