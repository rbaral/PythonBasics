__author__ = 'rbaral'

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
    names1880 = pd.read_csv('data/ssa_baby_names/yob1880.txt', names=['name', 'sex', 'births'])
    return names1880

names1880 = readDataFile()
#print names1880
# count the birth by the gender
birth_count_gender = names1880.groupby('sex').births.sum()
#print birth_count_gender
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
#print total_births
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
print top1000
#print top1000[top1000['year']==2015][:10]
# get the boys data from top1000
boys = top1000[top1000.sex == 'M']
# total number of births by year and name
total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
#print total_births
# subset it to some names
subset = total_births[['John', 'Harry', 'Mary']]
#print subset
#plot the subset
#plt.show(subset.plot(figsize=(12, 10), title="Number of births per year"))
# proportion of the births represented by the top 1000 most popular names
#table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
# plot the table
#plt.show(table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10)))
df = boys[boys.year == 2010]
# find how many of the prop records are required to reach 0.5. We can use the cumulative sum to do this
prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()
#print prop_cumsum.searchsorted(0.5) # this gives the no. of elements in the prop list excluding the first index (0) of the list
def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().searchsorted(q) + 1
diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
#print diversity.head
#plot the diversity dataframe
#plt.show(diversity.plot(title="Number of popular names in top 50%"))

'''
see the effect of change of the last letter
of the names
'''
def lastLetterRevolution():
    # extract last letter from name column
    get_last_letter = lambda x: x[-1]
    last_letters = names.name.map(get_last_letter)
    last_letters.name = 'last_letter'
    table = names.pivot_table('births', index=last_letters, columns=['sex', 'year'], aggfunc=sum)
    subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
    #print subtable.head()
    #find the proportion of the usage of the letters
    letter_prop = subtable/ subtable.sum().astype(float)
    #print letter_prop
    #fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    #plt.show(letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male'))
    #plt.show(letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False))
    #normalize by the year and sex and select a subset of letters for the boy names to get a time-series
    letter_prop = table / table.sum().astype(float)
    dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
    plt.show(dny_ts.plot())

#lastLetterRevolution()

'''
analyze the names that were common to boys
before and later to girls
'''
def boyNamesChangedToGirlNames():
    all_names = top1000.name.unique()
    # get the names that start with 'lesl'
    mask = np.array(['lesl' in x.lower() for x in all_names])
    lesley_like = all_names[mask]
    #print lesley_like
    # filter the dataframes that have the 'lesl' keywords
    filtered = top1000[top1000.name.isin(lesley_like)]
    #print filtered.groupby('name').births.sum()
    # aggregate by sex and year
    table = filtered.pivot_table('births', index='year', columns='sex', aggfunc='sum')
    # normalize
    table = table.div(table.sum(1), axis=0)
    #print table.tail()
    # plot it
    plt.show(table.plot(style={'M': 'k-', 'F': 'k--'}, title ="Proportion of male/female Lesley-like names over time"))


#boyNamesChangedToGirlNames()


