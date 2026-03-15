import time
import numpy as np
import serial
import parallel 
import optimized
import os
import matplotlib.pyplot as plt
import pandas as pd

# Constants
NUM_OF_WORKERS = [2, 4, 8]                      # number of processors working in parallel
                                                # no need to test for 1 processor (serial)

if(os.cpu_count() > 8):
    NUM_OF_WORKERS.append(os.cpu_count())

def run_experiment(N):
    """ Run the experiment of matrix multiplication keeping track of the time taken
...     Args:
...         N (int): size of the matrices
...     Returns:
...         DataFrame: DataFrame of the resulting runtime results for all 3 possible implementations and all number of processors
...  """

    # Generate random matrices
    A = np.random.randint(0, 1000, size = (N, N))
    B = np.random.randint(0, 1000, size = (N, N))

    # Measure runtime using parallel processing implementation
    t_parallel = []
    for workers in NUM_OF_WORKERS:
        start_time = time.perf_counter()
        parallel.run_in_parallel(workers, A, B)
        end_time = time.perf_counter()
        t_parallel.append(end_time - start_time)

    # Measure runtime using nested loop implementation
    start_time = time.perf_counter()
    serial.multiply_matrices(A, B)
    end_time = time.perf_counter()
    t_serial = end_time - start_time

    # Measure runtime using numpy implementation
    start_time = time.perf_counter()
    optimized.multiply_matrices_optimized(A, B)
    end_time = time.perf_counter()
    t_optimized = end_time - start_time

    results = {
        'size' : NUM_OF_WORKERS,
        't_serial': t_serial,
        't_optimized': t_optimized,
        't_parallel': t_parallel
    }

    # Return a dataframe of results
    data = pd.DataFrame.from_dict(results)
    return data

def plot_compare(df, num):
    """ Produce a plot of the results given in a Dataframe
...     Args:
...         df (DataFrame): The dataframe to take data from
...         num (int): Number of the experiment
...  """

    fig, axs = plt.subplots(nrows = 1, ncols = 2)
    fig.suptitle(f"Comparing performance with different number of processors for dataset {num}")
    axs[0].plot(df['size'], df['t_parallel'], color = 'red')
    axs[0].set_xlabel("Number of processors")
    axs[0].set_ylabel("Runtime")
    axs[0].grid(True)

    speedup = df['t_serial'] / df['t_parallel']
    axs[1].plot(df['size'], speedup, color = 'red')
    axs[1].set_xlabel("Number of processors")
    axs[1].set_ylabel("Speedup")
    axs[1].grid(True)
    plt.tight_layout(h_pad = 1, w_pad = 1)
    plt.show()