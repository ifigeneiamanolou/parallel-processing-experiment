import concurrent.futures
import numpy as np

def set_row(A, B, i):
    """Compute a given row of the product of 2 matrices.
...     Args:
...         A (ndarray): First matrix.
...         B (ndarray): Second matrix.
            i (int) : Row index
...     Returns:
...         ndarray: One row of product of A and B.
...  """
    row = np.dot(A[i], B)
    return row

def run_in_parallel(max_workers, A, B):
    """Compute the product of 2 matrices with a given number of parallel processors
...     Args:
...         A (ndarray): First matrix.
...         B (ndarray): Second matrix.
            max_workers (int) : Number of parallel processors
...     Returns:
...         ndarray : The product of A, B as an ndarray
...  """
    with concurrent.futures.ProcessPoolExecutor(max_workers = max_workers) as executor:
        # Submit all tasks to the executor
        futures = [executor.submit(set_row, A, B, i) for i in range(A.shape[0])]
        # Store the matrix produced
        rows = [future.result() for future in futures]
        return np.array(rows)