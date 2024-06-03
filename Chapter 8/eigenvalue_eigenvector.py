import numpy as np

def power_method(A, num_simulations: int):
    x_k = np.random.rand(A.shape[1])
    for i in range(num_simulations):
        x_k1 = np.dot(A, x_k)
        x_k1_norm = np.linalg.norm(x_k1)
        x_k = x_k1 / x_k1_norm
    eigenvalue = np.dot(x_k.T, np.dot(A, x_k)) / np.dot(x_k.T, x_k)
    
    return eigenvalue, x_k

def inverse_power_method(A, num_simulations: int):
    x_k = np.random.rand(A.shape[1])
    
    A_inv = np.linalg.inv(A)
    
    for i in range(num_simulations):
        x_k1 = np.dot(A_inv, x_k)
        x_k1_norm = np.linalg.norm(x_k1)
        x_k = x_k1 / x_k1_norm
    eigenvalue_inv = np.dot(x_k.T, np.dot(A_inv, x_k)) / np.dot(x_k.T, x_k)
    
    smallest_eigenvalue = 1 / eigenvalue_inv
    
    return smallest_eigenvalue, x_k

def rayleigh_quotient_iteration(A, num_simulations: int, tol=1e-10):
    n = A.shape[0]
    b_k = np.random.rand(n)
    b_k = b_k / np.linalg.norm(b_k)
    mu_k = np.dot(b_k.T, np.dot(A, b_k))  

    for _ in range(num_simulations):
        try:
            b_k1 = np.linalg.solve(A - mu_k * np.eye(n), b_k)
        except np.linalg.LinAlgError:
            break

        b_k1 = b_k1 / np.linalg.norm(b_k1)
        
        mu_k1 = np.dot(b_k1.T, np.dot(A, b_k1))
        
        if np.abs(mu_k1 - mu_k) < tol:
            break
        
        b_k = b_k1
        mu_k = mu_k1
    
    return mu_k, b_k

A = np.array([[5, 1], [1, 5]])
eigenvalue, eigenvector = power_method(A, 10)
print("Dominant Eigenvalue:", eigenvalue)
print("Corresponding Eigenvector:", eigenvector)

smallest_eigenvalue, eigenvector = inverse_power_method(A, 1000)
print("Smallest Eigenvalue:", smallest_eigenvalue)
print("Corresponding Eigenvector:", eigenvector)

eigenvalue, eigenvector = rayleigh_quotient_iteration(A, 1000)
print("Eigenvalue:", eigenvalue)
print("Corresponding Eigenvector:", eigenvector)