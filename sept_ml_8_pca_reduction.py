from sklearn.decomposition import PCA
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1]])
pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_ratio_)