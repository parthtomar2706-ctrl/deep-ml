import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    data=np.array(data,dtype=float)
    mean=np.mean(data,axis=0)
    std=np.std(data,axis=0,ddof=0)
    std=np.where(std==0,1,std)
    stan=(data-mean)/std
    mi=np.min(data,axis=0)
    ma=np.max(data,axis=0)
    val=ma-mi
    val=np.where(val==0,1,val)
    norm=(data-mi)/val
    stan=np.round(stan,4)
    norm=np.round(norm,4)
    return stan,norm