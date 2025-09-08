import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1], [2]])
y = np.array([1, 2])
reg = LinearRegression().fit(X, y)
print(reg.score(X, y))