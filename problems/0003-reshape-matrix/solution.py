import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    res=[]
    row=len(a)
    col=len(a[0])
    if row*col!=new_shape[0]*new_shape[1]:
        return res
    res = np.array(a).reshape(new_shape).tolist()
    return res