from modules import file_IO, preprocessing
import numpy as np
import h5py

# Size of the data block to be averaged.
block_dims = np.array([4,4,4])

f = h5py.File("preprocessed/reduced.hdf5", "w")

def load_component(comp_name):
    """
    return: 1) array of shape n_train+n_test, comp_size
            2) n_train
    """
    data = file_IO.load_directory("set_train/"+comp_name+"/", block_dims)
    n_train = data.shape[0]
    data = np.concatenate((data,
                           file_IO.load_directory("set_test/" + comp_name + "/", block_dims)
                          ), axis = 0)
    return preprocessing.remove_zero_columns(data), n_train

data, n_train = load_component("")

f.create_dataset("train_data", data=data[:n_train, :])
f.create_dataset("test_data",  data=data[n_train:, :])
print("n train dataset: ", n_train)

f.close()
