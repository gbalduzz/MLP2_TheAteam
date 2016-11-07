import nibabel
import numpy as np
import os
import modules.preprocessing as prp
#from multiprocessing.pool import ThreadPool

def load_directory(dirname, block_length):
    """
    :param dirname: relative dir path
    :return: np. array with n_files, n_features dimensions
    """
    assert(len(block_length) == 3)

    path=os.getcwd()+"/"+dirname
    filenames = [name for name in os.listdir(path) if name.split('.')[-1]=='nii']
    n = len(filenames)
    #n = 10 #debug

    type = filenames[0].split('_')[0]
    assert(type == "train" or type=="test")
    sample_shape = nibabel.load(path+filenames[0]).shape
    four_d = (len(sample_shape) == 4)
    n_features = np.prod(sample_shape)/np.prod(block_length)
    x = np.zeros([n,n_features])

    #pool = ThreadPool(NUM_THREADS)
    for i in range(n): # work item
        filename = path+"/"+type+"_"+str(i+1)+".nii"
        data=nibabel.load(filename).get_data()
        if four_d: data = data[:,:,:,0]
        x[i]= np.ndarray.flatten(prp.block_data(data, block_length))

    return x


def sum_data(filename):
    file = nibabel.load(filename)
    return sum(np.ndarray.flatten(file.get_data()))

def sum_partial_data(filename, boundaries):
    file = nibabel.load(filename)
    data = file.get_data()[boundaries[0][0]:boundaries[0][1],boundaries[1][0]:boundaries[1][1], boundaries[2][0]:boundaries[2][1]]
    return sum(np.ndarray.flatten(data))
