import numpy as np

def min_histo(X,Y):
    def prod(x,y):
        return np.sum(np.amin(np.row_stack((x,y)), axis=0))

    print("computing kernel...")
    res = np.zeros([X.shape[0], Y.shape[0]])
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            res[i,j] = prod(X[i], Y[j])
    print("kernel computed.")
    return res
