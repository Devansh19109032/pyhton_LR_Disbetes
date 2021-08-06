from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression



iris = datasets.load_iris()
x = iris["data"][:, 3:]
y = (iris["target"] == 2).astype(np.int)
#print(y)
#print(x)
clf = LogisticRegression()
clf.fit(x,y)
t = clf.predict(([[2]]))
print(t)




#print(list(iris.keys()))
#print(iris['data'])
#print(iris['target'])
#print(iris['DESCR'])