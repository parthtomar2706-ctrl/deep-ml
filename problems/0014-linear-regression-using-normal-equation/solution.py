import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Convert input lists to NumPy arrays
    X_arr = np.array(X, dtype=float)
    y_arr = np.array(y, dtype=float).reshape(-1, 1)
    
    # Apply the normal equation: theta = (X^T * X)^(-1) * X^T * y
    theta = np.linalg.inv(X_arr.T @ X_arr) @ X_arr.T @ y_arr
    
    # Round to 4 decimal places, flatten to 1D, and convert to list
    return np.round(theta, 4).flatten().tolist()