from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
iris=load_iris()
print(iris.data)     
print(iris.feature_names)
print(iris.target)
print(iris.data.shape)
print(iris.target.shape)
X=iris.data
y=iris.target
knn=KNeighborsClassifier(n_neighbors=1)
print(knn)
knn.fit(X,y)
w=knn.predict([[3,5,4,2]])
print(w)
