import pandas as pd
from sklearn.externals import joblib

# load training model from file
clf = joblib.load('MPLClassifier')

# read
X1 = pd.read_csv('posi.csv')
y_predict1 = clf.predict(X1)
print(y_predict1)


X2 = pd.read_csv('nega.csv')
y_predict2 = clf.predict(X2)
print(y_predict2)