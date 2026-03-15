import numpy as np

def multiply_matrices(A, B):
     """Multiply two matrices using multiple nested loops.
...     Args:
...         A (ndarray): First matrix.
...         B (ndarray): Second matrix.
...     Returns:
...         ndarray : Product of A and B.
...  """
     m = len(A)             # number of rows of A
     r = len(A[0])          # number of columns of A or rows of B
     n = len(B[0])          # number of columns of B
     result = np.zeros(shape = (m, n))

     for i in range(m):
          for j in range(n):
               for k in range(r):
                    result[i][j] += A[i][k] * B[k][j]

     return result