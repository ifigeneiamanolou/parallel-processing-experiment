import numpy as np

def multiply_matrices_optimized(A, B):
    """Multiply two matrices using NumPy built-in function.
...     Args:
...         A (ndarray): First matrix.
...         B (ndarray): Second matrix.
...     Returns:
...         ndarray: Product of A and B.
...  """

    return np.matmul(A, B)