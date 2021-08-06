import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


iris = datasets.load_iris()
print(iris.DESCR)
features = iris.data
labels = iris.target
print(features[0],labels[0])

clf = KNeighborsClassifier()
clf.fit(features,labels)
pred = clf.predict([[1,2,3,1]])
