'''
this file illustrates different graphs
that are creating with pandas and matplotlib

Ref:
https://pandas.pydata.org/pandas-docs/stable/visualization.html
http://pandas.pydata.org/pandas-docs/version/0.19.0/visualization.html#box-plots
http://machinelearningmastery.com/quick-and-dirty-data-analysis-with-pandas/
https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def makeBoxplot():
    stratifying_vals = np.random.uniform(0, 100, 20)
    price_vals = np.random.normal(100, 5, 20)
    df = pd.DataFrame({'stratifying_var': stratifying_vals,
                       'price': price_vals})
    df['quartiles'] = pd.qcut(df['stratifying_var'], 4, labels=['0-25%', '25-50%', '50-75%',
                                                                '75-100%'])
    print(stratifying_vals)
    print(price_vals)
    #color = dict(boxes='DarkGreen', whiskers='DarkOrange',medians = 'DarkBlue', caps = 'Gray')
    df.boxplot(column='price', by='quartiles')
    plt.show()

def makeBasicgraph():
    ts = pd.Series(np.random.randn(10), index=pd.date_range('1/1/2000', periods=10))
    print(ts)
    ts = ts.cumsum()
    print(ts)
    ts.plot()
    plt.show()


if __name__=="__main__":
    print("main started")
    #makeBasicgraph()
    makeBoxplot()