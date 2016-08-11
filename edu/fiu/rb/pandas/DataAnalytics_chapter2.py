__author__ = 'rbaral'

import json
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read the json data file.
# the data files is taken from the Python for Data Analysis book
path = 'data/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
#create the pandas Dataframe from the records, using the key-values in the JSON file
frame = DataFrame(records)
# print all the entries with the timezone value
#print frame['tz'][:10]
# count the unique tz values
tz_counts = frame['tz'].value_counts()
#print tz_counts
# plot the data
clean_tz = frame['tz'].fillna('Missing') # fill the na values with the workd 'Missing'
clean_tz[clean_tz == ''] = 'Unknown' # fill the blanks with the 'Unknown' word
tz_counts = clean_tz.value_counts()
#print tz_counts[:10]
# plot the count of the timezone in a bar graph
#plt.show(tz_counts[:10].plot(kind='barh', rot=0))
# get the first word from the 'a' column
results = Series([x.split()[0] for x in frame.a.dropna()])
#print results[:5]
# get the non null data
cframe = frame[frame.a.notnull()]
# compute a value whether each row is Windows or not by comparing it to 'a' column
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows', 'Not Windows')
#print operating_system[:5]
# group data by its time zone column and the new list of operating systems
by_tz_os = cframe.groupby(['tz', operating_system])

# The group counts, analogous to the value_counts function above, can be computed
# using size. This result is then reshaped into a table with unstack:
agg_counts = by_tz_os.size().unstack().fillna(0)
#print agg_counts[:12]
# let's select the top overall time zones.
# To do so, I construct an indirect index array from the row counts in agg_counts:
# sort in ascending order
indexer = agg_counts.sum(1).argsort()
#print indexer[:10]
# select the rows in that order, then slice off the last 10 rows
count_subset = agg_counts.take(indexer)[-10:]
#print count_subset
# plot it as a bar plot
#plt.show(count_subset.plot(kind='barh', stacked=True))
# plot the normalized values
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
#plt.show(normed_subset.plot(kind='barh', stacked=True))