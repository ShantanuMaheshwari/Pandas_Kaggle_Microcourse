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
"""Accessing column data in dataframe, accessing country column"""
print(reviews.country)
print(reviews['country'])
print(reviews.country[0])

# %%
"""Indexing of Dataframe"""
# Index Based Selection
print(reviews.iloc[0, :])               # Printing first row
print(reviews.iloc[0:2, :])             # Printing first, second row



