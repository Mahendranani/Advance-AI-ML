from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(random_state=1, max_iter=300).fit([[0,0],[1,1]], [0,1])
print(clf.predict([[2., 2.]]))