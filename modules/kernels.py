import numpy as np

def min_histo(X,Y):
    def prod(x,y):
        p = 0
        for i in range(len(x)): p += min(x[i], y[i])
        return p

    res = np.zeros([X.shape[0], Y.shape[0]])
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            res[i,j] = prod(X[i], Y[j])
    return res
