import numpy as np
import pandas as pd
import nltk
import yaml
import re

import pymongo
from pymongo import MongoClient


class Transition(object):
    """"""


class MarkovModel(object):

def get_data(cursor):
    attributes = ['slug', 'synopsis']
    results = []
    for i, x in enumerate(cursor):
        results.append([x[k] for k in attributes])

    df = pd.DataFrame(results, columns=attributes)
    return df

def test_anime_synopsis(n_synopsis, order):
    client = MongoClient()
    db = client.kitsu
    cursor = db.anime.find()
    df = get_data(cursor)
    words = ' '.join([s for s in df.synopsis.values[-n_synopsis:]]).split()
    mm = MarkovModel(words, order=order)
    return mm



if __name__ == '__main__':
    mm = test_anime_synopsis(n_synopsis=10000, order=4)
    print(mm.generate_text(50))
