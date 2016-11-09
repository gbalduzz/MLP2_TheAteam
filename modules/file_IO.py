import nibabel
import numpy as np
import os
import modules.preprocessing as prp
#from multiprocessing.pool import ThreadPool
def crop(x):
    return x[19:154, 24:186, 8:152]


def load_directory(dirname, n_blocks, n_bins):
    """
    :param dirname: relative dir path
    :return: np. array with n_files, n_features dimensions
    """
    assert(len(n_blocks) == 3)

    path=os.getcwd()+"/"+dirname
    filenames = [name for name in os.listdir(path) if name.split('.')[-1]=='nii']
    n = len(filenames)

    type = filenames[0].split('_')[0]
    assert(type == "train" or type=="test")
    sample_shape = nibabel.load(path+filenames[0]).shape
    four_d = (len(sample_shape) == 4)
    n_features = np.prod(n_blocks)*n_bins
    x = np.zeros([n,n_features])

    #pool = ThreadPool(NUM_THREADS)
    for i in range(n): # work item
        filename = path+"/"+type+"_"+str(i+1)+".nii"
        data=nibabel.load(filename).get_data()
        if four_d: data = data[:,:,:,0]
        x[i]= prp.concatenate_hystogram(prp.blocks(crop(data), n_blocks), n_bins)

    return x


def sum_data(filename):
    file = nibabel.load(filename)
    return sum(np.ndarray.flatten(file.get_data()))

def sum_partial_data(filename, boundaries):
    file = nibabel.load(filename)
    data = file.get_data()[boundaries[0][0]:boundaries[0][1],boundaries[1][0]:boundaries[1][1], boundaries[2][0]:boundaries[2][1]]
    return sum(np.ndarray.flatten(data))
