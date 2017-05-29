__author__ = 'rbaral'

#ref:http://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/

'''
Analyze the US baby names from the
SSA dataset. Can be used to analyze for different
metrics as provided in https://www.ssa.gov/oact/babynames/decades/names2010s.html
'''
'''
TODOS:
1) given a year, find the top N male, female names
2) top N popular names for year range (extension of 1)
3) trend in the names for every 5 years (which one decreased, which one increased)
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
read a sample csv file
'''
def readDataFile():
    # read the name file for the year 2015
    names1880 = pd.read_csv('data/ssa_baby_names/yob1880_small.txt', names=['name', 'sex', 'births'])
    return names1880

df = readDataFile()


'''
merge all the data files and get
a single dataframe
'''
def mergeDataFiles():
    # merge the data files from all the year and add the year column to the merged data
    years = range(1880,2016)
    pieces = []
    # the fields to be read
    columns = ['name', 'sex', 'births']
    # iterate through all the files
    for year in years:
        # dynamically get the names of the files
        path = 'data/ssa_baby_names/yob%d.txt'%year
        # read the content of the file into a data frame
        frame = pd.read_csv(path, names = columns)
        # append the year in the dataframe
        frame['year'] = year
        # append the content of the files in a list
        pieces.append(frame)
    # now concatenate everything into a single DataFrame
    names = pd.concat(pieces, ignore_index=True)
    return names

names = mergeDataFiles()
#print names[-10:]
# total births by year in each gender
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
print total_births
# plot the birth count by year for each gender
#plt.show(total_births.plot(title='Total births by sex and year'))

'''
let's insert a column prop with the fraction of babies given each name relative to
the total number of births. A prop value of 0.02 would indicate that 2 out of every 100
babies was given a particular name. Thus, we group the data by year and sex, then add
the new column to each group:
'''
def add_prop(group):
    # Integer division floors
    births = group.births.astype(float)
    # the fraction of births which got this name
    group['prop'] = births / births.sum()
    return group

# group the names by year and gender
names_grouped = names.groupby(['year', 'sex'])
# apply the function add_prop
names_prop = names_grouped.apply(add_prop)
#print names_prop[:10]
# sanity check for grouping, to verify that the prop column sums to 1 within all the groups
#print np.allclose(names_prop.groupby(['year', 'sex']).prop.sum(), 1)

'''
get top 1000 names for each sex/year combination
'''
def getTop1000():
    pieces = []
    for year, group in names_prop.groupby(['year', 'sex']):
        pieces.append(group.sort_values(by='births', ascending=False)[:1000])
    top1000 = pd.concat(pieces, ignore_index=True)
    return top1000

top1000 = getTop1000()
#print top1000


import datetime
'''
print "started1:",str(datetime.datetime.now())
df_agg = df.groupby(['sex','name']).agg({'births':sum})
'''
'''
#print df_agg
g = df_agg['births'].groupby(level=0, group_keys=False)
res = g.apply(lambda x: x.order(ascending=False).head(3))
print "completed1:",str(datetime.datetime.now())
print res
'''
print "****"
'''
pieces = []
for name, group in df.groupby(['sex']):
	pieces.append(group.sort_values(by=['births'], ascending=False)[:3])
res = pd.concat(pieces, ignore_index=True)
'''
#print res

'''
#add new column to each group
def add_prop(group):
    # Integer division floors
    births = group.births.astype(float)
    print births.sum()
    # the fraction of births which got this name
    group['prop'] = births.sum() #births / births.sum()
    return group

#find total within a group
#df_agg = df.groupby(['sex']).agg({'births':sum})
print "started2:",str(datetime.datetime.now())
# group the names by year and gender
names_grouped = df.groupby(['sex'])
# apply the function add_prop
names_prop = names_grouped.apply(add_prop)
print "completed2:",str(datetime.datetime.now())
print names_prop
'''
