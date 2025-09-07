from sklearn.tree import DecisionTreeClassifier
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = DecisionTreeClassifier().fit(X, y)
print(clf.predict([[2, 2]]))