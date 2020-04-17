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
"""Getting column names from dataframe"""
print(reviews.columns)

# %%
"""Accessing column data in dataframe, accessing country column"""
print(reviews.country)
print(reviews['country'])
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
# del reviews2

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

#%%
"""Condition Selection (isin())"""
# Printing rows where country in ['Italy', 'France']
print(reviews.loc[reviews['country'].isin(['Italy', 'France'])])
"""Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines
 from Australia or New Zealand."""
top_oceania_wines = reviews.loc[(reviews['points']>=95) & (reviews['country'].isin(['Australia', 'New Zealand']))]

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
reviews2['index_bckwds'] = range(len(reviews2)-1, 0-1, -1)
print(reviews2)

# %%
"""End of Indexing, Selecting, Assigning"""
# Deleting extra dataframes
del dataframe2
del dataframe3
del top_oceania_wines

# %%