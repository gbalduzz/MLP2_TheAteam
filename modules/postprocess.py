import numpy as np

def format(data, filename='final_prediction.csv'):
    tag = np.array(range(1,len(data)+1), dtype=np.int32)
    #mytype = np.dtype([('ID', np.int32), ('prediction', np.int32)])
    #out = np.rec.fromarrays((id,data), dtype=mytype)
    out = np.column_stack((tag, data))
    np.savetxt(filename, out, fmt="%d",
               delimiter=',', header="ID,prediction", comments='')
