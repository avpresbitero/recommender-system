# fuzz is used to compare TWO strings
from fuzzywuzzy import fuzz

# process is used to compare a string to MULTIPLE other strings
from fuzzywuzzy import process


def get_list_movies_to_keep(df_ratings, thresh=50):
    df_ratings_group = df_ratings[df_ratings.rating != 0].groupby('movieId')['userId'].count().reset_index()
    keep_movies = df_ratings_group[df_ratings_group.userId > thresh].movieId.tolist()
    return keep_movies

def get_list_users_to_keep(df_ratings, thresh=50):
    df_ratings_group = df_ratings[df_ratings.rating != 0].groupby('userId')['movieId'].count().reset_index()
    keep_users = df_ratings_group[df_ratings_group.movieId > thresh].userId.tolist()
    return keep_users

def pivot_dataframe(df_ratings):
    df_movie_features = df_ratings.pivot(index='movieId',
                                         columns='userId',
                                         values='rating').fillna(0)
    return df_movie_features

def get_ratio(row, search):
    name = row['title']
    return fuzz.token_sort_ratio(name, search)


def get_fuzzy_movie_index(df, search, thresh=70):
    title = df.loc[df.apply(get_ratio, args=(search, ), axis=1) > thresh,
                   "title"].tolist()[0]
    movie_id = df.loc[df['title'] == title, 'movieId'].iloc[0]
    idx = df.index[df['movieId']==movie_id].tolist()[0]
    return idx

def make_recommendation(model_knn, data, fav_movie, n_recommendations, df_movies):
    
    # fit
    model_knn.fit(data)
    
    # get input movie index
    print('You have input movie:', fav_movie)
    
    idx = get_fuzzy_movie_index(df_movies, fav_movie)
    
    print('Recommendation system start to make inference')
    print('......\n')
    distances, indices = model_knn.kneighbors(data[idx], n_neighbors=n_recommendations+1)
#     print (distances, indices.squeeze().tolist())
    for i, distance in enumerate(distances.squeeze().tolist()):
        moviedx = indices.squeeze().tolist()[i]
        print (f'{df_movies.loc[[moviedx]].title.values[0]} with distance : {distance}')
