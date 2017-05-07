from sklearn.linear_model import LogisticRegression

from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib


import pandas as pd

X, y = load_iris(True)

df = pd.read_csv("iris.csv")
X = df.iloc[]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

lr = LogisticRegression(penalty='l2', solver='newton-cg', max_iter=200)

lr_fit = lr.fit(X_train, y_train)

est = lr.predict(X_test)

s = 0
for e, t in zip(est, y_test):
	if e == t:
		s = s + 1
print('test_accuracy={}'.format(s / len(y_test)))

print(est)
print(y_test)

print(lr)


