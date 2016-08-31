__author__='rbaral'
'''
Ref: http://pbpython.com/pandas-pivot-table-explained.html
'''

import pandas as pd
import numpy as np


def readFile():
	df = pd.read_excel("sales-funnel.xlsx")
	#print df.head()
	return df

#this method didn't work in pandas 0.17
def defineColumn():
	'''
	define the status column as a category and set the order
	we want to see
	'''
	df = readFile()
	df["Status"] = df["Status"].astype("category")
	print df
	print df["Status"].cat.set_categories(["won","pending","presented","declined"],inplace=True)
	#print df


def pivotData():
	'''
	pivot the data using different methods
	'''
	df = readFile()
	#single index
	#print pd.pivot_table(df,index=["Name"])
	#multiple index
	#print pd.pivot_table(df, index=["Manager","Rep"])
	#print pd.pivot_table(df, index=["Manager","Rep"],values=["Price"])
	#print pd.pivot_table(df, index=["Manager","Rep"],values=["Price"],aggfunc=np.count_nonzero)
	#print pd.pivot_table(df, index=["Manager","Rep"],values=["Price"], columns=["Product"],aggfunc=[np.sum], fill_value=0)
	#print pd.pivot_table(df, index=["Manager","Rep"],values=["Price", "Quantity"], columns=["Product"],aggfunc=[np.sum], fill_value=0)
	#margins=True for the sum of all the rows
	#print pd.pivot_table(df,index=["Manager","Rep","Product"],values=["Price","Quantity"],aggfunc = [np.sum],fill_value=0, margins=True)
	#pass the dictionary of aggfunc so that we can apply different functions to different values we selected
	table = pd.pivot_table(df,index=["Manager","Status"],columns=["Product"],values=["Quantity","Price"],aggfunc={"Quantity":len,"Price":np.sum},fill_value=0)
	#print table.query('Manager ==["Debra Henley"]')
	print table.query('Manager ==["Debra Henley"] & (Status==["pending","won"])')
if __name__=="__main__":
	print "started main"
	#readFile()
	#defineColumn()
	pivotData()
	