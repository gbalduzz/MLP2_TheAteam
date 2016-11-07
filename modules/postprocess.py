import numpy as np

def format(data, filename='final_prediction.csv'):
    id = np.array(range(1,138+1), dtype=np.int32)
    mytype = np.dtype([('ID', np.int32), ('prediction', np.float64)])
    out = np.rec.fromarrays((id,data), dtype=mytype)
    #print(out)
    #print(out[0][0].dtype)
    np.savetxt(filename, out, fmt=["%.d","%.2f"],
               delimiter=',', header="ID,prediction", comments='')
