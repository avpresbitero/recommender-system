# Recommender Systems

“We are leaving the age of information and entering the age of recommendation.”


Reference: https://towardsdatascience.com/intro-to-recommender-system-collaborative-filtering-64a238194a26

Common approaches to collaborative filtering are as follows: 

1. Nearest Neighborhood
2. Matrix Factorization


Like many machine learning techniques, a recommender system makes prediction based on users’ historical behaviors. Specifically, it’s to predict user preference for a set of items based on past experience. To build a recommender system, the most two popular approaches are Content-based and Collaborative Filtering.

Content-based approach requires a good amount of information of items’ own features, rather than using users’ interactions and feedbacks. For example, it can be movie attributes such as genre, year, director, actor etc., or textual content of articles that can extracted by applying Natural Language Processing.

Collaborative Filtering, on the other hand, doesn’t need anything else except users’ historical preference on a set of items. Because it’s based on historical data, the core assumption here is that the users who have agreed in the past tend to also agree in the future. In terms of user preference, it usually expressed by two categories. Explicit Rating, is a rate given by a user to an item on a sliding scale, like 5 stars for Titanic. This is the most direct feedback from users to show how much they like an item. Implicit Rating, suggests users preference indirectly, such as page views, clicks, purchase records, whether or not listen to a music track, and so on.

This repository is dedicated to RS. 