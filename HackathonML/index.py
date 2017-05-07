# -*- coding:utf-8 -*-  

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from sklearn import cluster, cross_validation, tree
# from itertools import izip
# import 

np.random.seed(123)

iris = pd.read_csv("iris.csv")

print(iris.shape)
print(iris.head())

print(iris.describe().T) # 统计性描述

irisK3 = cluster.KMeans(n_clusters=3, random_state=1)
irisFeatures = iris.ix[:,1:4]
irisK3.fit(irisFeatures)
print(irisK3.labels_)



target = iris["Name"]
data = iris.ix[:,1:4]
# 分成训练集、测试集
train_data,test_data,train_target,test_target=cross_validation.train_test_split(data, target, test_size=0.24, random_state=0)

clf = tree.DecisionTreeClassifier(criterion='gini', max_depth=6, min_samples_split=5)
clf_fit = clf.fit(train_data, train_target)
print(clf_fit)

train_est = clf.predict(train_data) # 预测训练集
test_est = clf.predict(test_data) # 预测测试集
sum = 0

# for est, target in izip(test_est,test_target):
# 	if est == target:
# 		sum = sum + 1
# print('test_accuracy={}'.format(sum * 1.0/36*100))

# sum = 0
# for est, target in izip(train_est,train_target):
# 	if est == target:
# 		sum = sum + 1
# print('train_accuracy={}'.format(sum * 1.0/114*100))
