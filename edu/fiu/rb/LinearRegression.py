__author__ = 'rbaral'
import sklearn
print sklearn.__version__

from sklearn.linear_model import LinearRegression
# Training data
X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]
# Create and fit the model
model = LinearRegression()
model.fit(X, y)
for i in range(21):
    print 'A %d" pizza should cost: $%.2f' %(i, model.predict([i])[0])
