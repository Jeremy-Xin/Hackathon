from __future__ import division

from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib

import pandas as pd

df = pd.read_csv("data_inuse.csv")
X = df.iloc[:, 0:6]
y = df.iloc[:, 6]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# clf = LogisticRegression(penalty='l2', solver='newton-cg', max_iter=400)
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, activation='logistic',
                    hidden_layer_sizes=(15,), random_state=1, learning_rate='adaptive',
                    max_iter=400)

clf.fit(X_train, y_train)
y_est = clf.predict(X_test)

posi_data = pd.DataFrame()
nega_data = pd.DataFrame()

positive_test = 0
positive_est = 0
correct = 0
for idx in xrange(len(y_test)):
	if y_test.iloc[idx] == y_est[idx]:
		correct = correct + 1
	if y_test.iloc[idx]:
		positive_test = positive_test + 1
	if y_est[idx]:
		positive_est = positive_est + 1
	if y_test.iloc[idx] and y_est[idx]:
		posi_data = posi_data.append(X_test.iloc[idx])
	if not y_test.iloc[idx] and not y_est[idx]:
		nega_data = nega_data.append(X_test.iloc[idx])


print('accuracy={}'.format(correct / len(y_test)))
print('correct={}'.format(correct))
print('positive_test={}'.format(positive_test))
print('positive_est={}'.format(positive_est))


columns = ['temperature','blood_pressure','heart_rate','breathing_rate', 'vertical_speed', 'horizontal_speed']
posi_data.to_csv('posi.csv', columns=columns, index=False, sep=',')
nega_data.to_csv('nega.csv', columns=columns, index=False, sep=',')
joblib.dump(clf, "MPLClassifier")
