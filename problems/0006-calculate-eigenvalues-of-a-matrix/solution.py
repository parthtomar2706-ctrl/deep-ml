import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a,b=matrix[0]
    c,d=matrix[1]
    trace=(a+d)
    det=a*d-b*c
    discriminant=trace**2-4*det
    if discriminant < 0:
        raise ValueError("Matrix has complex eigenvalues.")
    sqrt_discriminant = math.sqrt(discriminant)
    eigenvalue1 = (trace + sqrt_discriminant) / 2
    eigenvalue2 = (trace - sqrt_discriminant) / 2

    eigenvalues = sorted([eigenvalue1, eigenvalue2], reverse=True)
    return eigenvalues