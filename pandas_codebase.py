"""
Created by Shantanu Maheshwari on 2:47 PM 16/04/20.
Usage: Kaggle Pandas Micro-course codes
"""
# %%
"""Importing Libraries"""
import pandas as pd

# %%
"""Creating Dataframe"""
dataframe1 = pd.DataFrame({'Ram': ['I liked it', 'It was awful'],
                           'Shyam': ['Pretty good', 'Bland']},
                          index=['Product A', 'Product B'])

# %%
"""Creating Series"""
series1 = pd.Series([30, 40, 50], index=['Sales 2017', 'Sales 2018', 'Sales 2019'], name='Sales')
print(series1)

# %%
"""Reading Wines Dataset"""
reviews = pd.read_csv('./Data/winemag-data-130k-v2.csv', index_col=0)
reviews.head()

# %%
"""Printing n=10 rows using head"""
reviews.head(10)

# %%
"""End of Creating, Reading and Writing"""
# Deleting extra variables
del dataframe1
del series1

# %%
"""Getting column names from dataframe"""
print(reviews.columns)

# %%
"""Accessing column data in dataframe, accessing country column"""
print(reviews.country)
print(reviews['country'])
# Printing country value of the first row
print(reviews.country[0])

# %%
"""Index based Indexing of Dataframe"""
print('First Row\n', reviews.iloc[0, :])  # Printing first row
print('First, Second Row\n', reviews.iloc[0:2, :])  # Printing first, second row
print('First Column\n', reviews.iloc[:, 0])  # Printing first column
print('First, Second column\n', reviews.iloc[:, 0:2])  # Printing first, second column

# %%
"""Label based Indexing of Dataframe"""
"""NOTE:    iloc[0:2] '2' is not included so returns 2 values
            loc[0:2] '2' is also included so returns 3 values  
"""
# Printing first row
print('First Row\n', reviews.loc[0, :])
# Printing first, second row
print('First, Second, Third Row\n', reviews.loc[0:2, :])
# Printing first column
print('First Column\n', reviews.loc[:, 'country'])
# Printing first, second column
print('First, Second column\n', reviews.loc[:, ['country', 'description']])
# Selecting records with index labels = [1, 2, 3, 5, 8]
print('Printing records with index = [1, 2, 3, 5, 8]\n', reviews.iloc[[1, 2, 3, 5, 8], :])

# %%
"""Create a variable df containing the country, province, region_1, and region_2 columns
 of the records with the index labels 0, 1, 10, and 100."""
dataframe2 = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]
"""Create a variable df containing the country and variety columns of the first 100 records"""
dataframe3 = reviews.loc[0:99, ['country', 'variety']]

# %%
"""Manipulating index"""
# Setting 'title' column as index
reviews2 = reviews.set_index('title')
del reviews2

# %%
"""Condition Selection (==, &, |)"""
# Printing whether country is "Italy" or not
print(reviews['country'] == 'Italy')
# Printing only those rows where country == "Italy"
print(reviews.loc[reviews['country'] == 'Italy'])
# Printing rows where country == "Italy" and points >= 90
print(reviews.loc[(reviews['country'] == 'Italy') & (reviews['points'] >= 90)])
# Printing rows where country == "Italy" or points >= 90
print(reviews.loc[(reviews['country'] == 'Italy') | (reviews['points'] >= 90)])

# %%
"""Condition Selection (isin())"""
# Printing rows where country in ['Italy', 'France']
print(reviews.loc[reviews['country'].isin(['Italy', 'France'])])
"""Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines
 from Australia or New Zealand."""
top_oceania_wines = reviews.loc[(reviews['points'] >= 95) & (reviews['country'].isin(['Australia', 'New Zealand']))]

# %%
"""Condition Selection (Handling Null Values)"""
# Printing rows where price is given (price is not null)
print(reviews.loc[reviews['price'].notnull()])
# Printing rows where price is not given
print(reviews.loc[reviews['price'].isnull()])

# %%
"""Assigning Data"""
# Making copy of dataframe for making modifications
reviews2 = reviews.copy()
# Adding constant value: Adding a new column 'critic' with data: 'everyone' in each row
reviews2['critic'] = 'everyone'
# Adding iterable of values: Adding a new column 'index_bckwds' with reverse of index
reviews2['index_bckwds'] = range(len(reviews2) - 1, 0 - 1, -1)
print(reviews2)

# %%
"""End of Indexing, Selecting, Assigning"""
# Deleting extra dataframes
del dataframe2
del dataframe3
del top_oceania_wines

# %%
"""Summary Functions"""
reviews.describe()

# %%
"""Mean values"""
reviews['points'].mean()

# %%
"""Median values"""
reviews['points'].median()

# %%
"""To get unique values in a column"""
reviews['taster_name'].unique()
# OR set(reviews['taster_name']

# %%
"""Count how many times a value occurs"""
reviews['taster_name'].value_counts()

# %%
"""MAP function"""
# suppose that we wanted to remean the scores the wines received to 0
reviews_points_mean = reviews['points'].mean()
print(reviews['points'].map(lambda x: x - reviews_points_mean))
print(pd.Series(map(lambda x: x - reviews_points_mean, reviews['points'])))

# %%
"""APPLY function"""
# suppose that we wanted to remean the scores the wines received to 0
def remean_points(row):
    row['points'] -= reviews_points_mean
    return row

reviews.apply(remean_points, axis='columns')

# %%
"""Combining two or more columns into one"""
country_region_1 = reviews['country'] + ' - ' + reviews['region_1']
print(country_region_1)
del country_region_1

# %%
"""I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable bargain_wine 
with the title of the wine with the highest points-to-price ratio in the dataset."""
best_points_to_price_ratio = (reviews.points / reviews.price).max()
print("Best points to price ratio: ", best_points_to_price_ratio)
bargain_wine = reviews.loc[reviews['points'] / reviews['price'] ==
                           best_points_to_price_ratio].loc[:, ['title', 'points', 'price']]
print(bargain_wine)
del best_points_to_price_ratio
del bargain_wine

# %%
"""There are only so many words you can use when describing a bottle of wine. Is a wine more likely to be
 "tropical" or "fruity"? Create a Series descriptor_counts counting how many times each of these two words appears
  in the description column in the dataset."""
n_tropical = sum(reviews['description'].map(lambda desc: 'tropical' in desc))
n_fruity = sum(reviews['description'].map(lambda desc: 'fruity' in desc))
print(pd.Series(data=[n_tropical, n_fruity], index=['tropical', 'fruity']))
del n_tropical
del n_fruity

# %%
"""We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard 
to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars,
 a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.
Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically
 get 3 stars, regardless of points."""
def star_rating(country, points):
    if country == 'Canada':
        return 3
    elif points >= 95:
        return 3
    elif points >= 85:
        return 2
    else:
        return 1
# Using MAP function
print(pd.Series(map(star_rating, reviews['country'], reviews['points'])))

def star_rating(row):
    if row['country'] == 'Canada':
        return 3
    elif row['points'] >= 95:
        return 3
    elif row['points'] >= 85:
        return 2
    else:
        return 1
print(reviews.apply(star_rating, axis='columns'))

# %%
"""End of Summary Functions and Maps"""
del reviews_points_mean

# %%