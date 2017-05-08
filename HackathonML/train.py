from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier


from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib


import pandas as pd

df = pd.read_csv("data.csv")
X = df.iloc[:, 0:6]
y = df.iloc[:, 6]

# print(X)
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# clf = LogisticRegression(penalty='l2', solver='newton-cg', max_iter=400)
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, activation='logistic',
                    hidden_layer_sizes=(15,), random_state=1, learning_rate='adaptive',
                    max_iter=400)


clf.fit(X_train, y_train)

y_est = clf.predict(X_test)

s = 0
for e, t in zip(y_est, y_test):
	if e == t:
		s = s + 1
print('test_accuracy={}'.format(s / len(y_test)))
print(clf)
print(y_est)
# print(y_test)
