import numpy as np

def remove_zero_columns(x,n_train,tollerance=0):
    """
    :param x: array to reduce, assumed positive
    :param tollerance: maximum abs value that is considered zero
    :return: np.array with removed columns
    """
    max_values = np.amax(x[:n_train,:], axis=0)
    mask = np.ones(max_values.shape)*tollerance
    keep_indices = np.greater(max_values,mask)
    return x[:, keep_indices]

max

def block_data(x, l):
    """
    :param x: array to reduce
    :param l: 3D vector of block lengths. must divide exactly x.shape
    :return:  return block sums of the x array
    """
    assert(((np.array(x.shape) % l == 0).all()))
    new_shape = np.array(x.shape) / l;
    res = np.zeros(new_shape)
    for i0 in range(new_shape[0]) :
        for i1 in range(new_shape[1]):
            for i2 in range(new_shape[2]):
                res[i0,i1,i2] = np.sum(np.ndarray.flatten(  x[ i0*l[0] : (i0+1)*l[0], i1*l[1] : (i1+1)*l[1], i2*l[2] : (i2+1)*l[2]]))

    return res
