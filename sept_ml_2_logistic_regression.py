from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=0).fit([[1],[2]], [0,1])
print(clf.predict([[1.5]]))