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


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



plt.scatter(X1.iloc[:30, 2], X1.iloc[:30, 3], color='red', marker='o', label='drowning', s=50)
plt.scatter(X2.iloc[:70, 2], X2.iloc[:70, 3], color='blue', marker='+', label='normal', s=50)

plt.xlabel('heart rate')
plt.ylabel('breathing rate')
plt.legend(loc=2)
plt.show()

