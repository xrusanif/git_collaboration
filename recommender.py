"""
contains various implementations for recommending movies
"""

import pandas as pd
from utils import movies, ratings


# recommender_systems_intro_filled.ipynb
def recommend_random(query, ratings, k=10):
    """
    Recommends a list of k random movie ids
    """
    return [1, 20, 34, 25]


# recommender_systems_intro_filled.ipynb
def recommend_popular(query, ratings, k=10):
    """
    Recommend a list of k movie ids that are the most popular
    """
    return []


# matrix_factorization_filled.ipynb
def recommend_nmf(query, model, ratings, k=10):
    """
    Recommend a list of k movie ids based on a trained NMF model
    """
    return []


# neighborhood_based_filtering.ipynb
def recommend_neighbors(query, model, ratings, k=10):
    """
    Recommend a list of k movie ids based on the most similar users
    """
    return []


if __name__=='__main__':
    # list of liked movies
    query = [1, 34, 56, 21]
    print(recommend_random(query, movies))
