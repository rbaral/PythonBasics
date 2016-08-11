__author__ = 'rbaral'

import pandas as pd
import matplotlib as plt
df = pd.read_csv('Camera.csv', sep=';') # read the file in which the columns are separated with semicolon
columns = ['Model', 'Date', 'MaxRes', 'LowRes', 'EffPix', 'ZoomW', 'ZoomT', 'NormalFR', 'MacroFR', 'Storage', 'Weight', 'Dimensions', 'Price']
df.columns = columns # the columns to be read from the file
df['Maker'] = df['Model'].apply(lambda s:s.split()[0]) # initialize a new column from the first word of the Model column
df=df[['Maker','Model','Date','MaxRes','LowRes','Weight','Dimensions','Price']].head()
print df[1:] # ignore the data type of the columns
print "---5 most recent models"
sorted_df = df.sort_values(['Date', 'Model'], ascending = [False, False]).head() # sort the values by 'Date' and 'Model' in descending order and return top 5 entries - head() will give default 5 entries
print sorted_df[1:]
#filtering entries by values
print "---selected entries by Price"
selected_Maker = df[df['Price'] >200]
print selected_Maker[1:]
#describe the statistics of the entries by their column
print "---description"
description_df =  df[['MaxRes','LowRes','Weight','Dimensions','Price']].describe()
print description_df
#an example of manually creating a dataframe and applying the filter
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'year': [2012, 2012, 2013, 2014, 2014],
        'reports': [4, 24, 31, 2, 3],
        'coverage': [25, 94, 57, 62, 70]}
df1 = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
print df1[df1['coverage'] > 90]
