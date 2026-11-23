import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    rowa=len(a)
    rowb=len(b)
    cola=len(a[0])
    colb=len(b[0])
    if cola!=rowb:
        return [[-1]]
    c=np.matmul(a,b)
    return c