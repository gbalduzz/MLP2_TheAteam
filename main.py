from modules import  preprocessing
import numpy as np
from sklearn import preprocessing, linear_model
from modules import postprocess
import h5py
import time

print("startup")

file = h5py.File("preprocessed/reduced.hdf5", "r")

#read the data
print("loading training set...")
train = np.array(file.get("train_data"))

y = np.loadtxt("targets.csv") # targets for train set

"""
#add feature from the ratio
def append_ratio(set, filename):
    ratio = np.loadtxt(filename).T
    return np.column_stack((set, ratio, ratio*ratio))
print("appending ratio")
train = append_ratio(train, "preprocessed/ratio_training.csv")
"""

# Scaling
scaler = preprocessing.StandardScaler().fit(train)
train = scaler.transform(train)

# Train the Model
start = time.clock()
print("start training")
regr = linear_model.SGDClassifier(n_iter=5, n_jobs=-1)
regr.fit(train,y)
finish = time.clock()
print("training time: ", finish-start)
del train

#print model parameters
#np.savetxt('wheights_output.csv', np.row_stack((regr.intercept_, regr.coef_)))


# Make Predictions and save
print("loading and making predictions")
test  = np.array(file.get("test_data"))
file.close()
#test = append_ratio(test, "preprocessed/ratio_testing.csv")
test = scaler.transform(test)

prediction = regr.predict(test)
postprocess.format(prediction, "predictions.csv")
print("done")
