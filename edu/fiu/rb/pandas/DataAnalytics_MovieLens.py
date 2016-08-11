__author__ = 'rbaral'

'''
analyze the Movie Lens dataset from
http://grouplens.org/datasets/movielens/
'''
import pandas as pd
# create the list of columns to be read from the user file
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
# read the user data file across the unames fields
users = pd.read_table('data/ml-1m/users.dat', sep='::', header=None,
names=unames)
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
# read the ratings data file across the rnames fields
ratings = pd.read_table('data/ml-1m/ratings.dat', sep='::', header=None,
names=rnames)
mnames = ['movie_id', 'title', 'genres']
# read the movies data file across the mnames fields
movies = pd.read_table('data/ml-1m/movies.dat', sep='::', header=None,
names=mnames)
#print movies[:10]
#Using pandas's merge function, we first merge ratings with
# users then merging that result with the movies data.
# pandas infers which columns to use as the merge (or join) keys based on overlapping names
merged_data = pd.merge(pd.merge(ratings, users), movies)
#print merged_data
#get mean movie ratings for each film grouped by gender, we can use the pivot_table method, where the index is for the rows
mean_ratings = merged_data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
#print mean_ratings[:9]
# group the data by title and use size() to get a Series of group sizes for each title
ratings_by_title = merged_data.groupby('title').size()
#print ratings_by_title[:10]
# find the titles with no. of ratings above 250
active_titles = ratings_by_title.index[ratings_by_title >= 250]
#print active_titles
# The index of titles receiving at least 250 ratings can then be used to select rows from mean_ratings above:
mean_ratings = mean_ratings.ix[active_titles]
#print mean_ratings
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
#print top_female_ratings[:10]
# find the movies that are most divisive between male and female viewers
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
#print sorted_by_diff[:10]
# find the most disagreement among viewers, independent of genders
# this can be done using the variance or standard deviation of ratings
rating_std_by_title = merged_data.groupby('title')['rating'].std()
# filter to the active titles
rating_std_by_title = rating_std_by_title.ix[active_titles]
# sort in descending order
rating_std_by_title = rating_std_by_title.order(ascending=False)
print rating_std_by_title[:10]