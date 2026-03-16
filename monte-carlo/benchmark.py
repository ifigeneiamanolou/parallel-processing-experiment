import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import time
import serial
import parallel
# Constants
NUM_OF_WORKERS = [2, 4, 8]                      # number of processors working in parallel
                                                # no need to test for 1 processor (serial)

if(os.cpu_count() > 8):
    NUM_OF_WORKERS.append(os.cpu_count())

def run_experiment(N, n):
    """ Run the experiment of producing multiple random walks
...     Args:
...         N (int) : number of random walk simulations
            n (int) : number of steps in each random walk
...     Returns:
...         DataFrame: DataFrame of the resulting runtime results for the 2 possible implementations and all number of processors
...  """

    # Measure runtime using parallel processing implementation
    t_parallel = []
    for workers in NUM_OF_WORKERS:
        start_time = time.perf_counter()
        parallel.run_in_parallel(workers, N, n)
        end_time = time.perf_counter()
        t_parallel.append(end_time - start_time)

    # Measure runtime using nested loop implementation
    start_time = time.perf_counter()
    serial.serial_monte_carlo(N, n)
    end_time = time.perf_counter()
    t_serial = end_time - start_time

    results = {
        'size' : NUM_OF_WORKERS,
        't_serial': t_serial,
        't_parallel': t_parallel
    }

    # Return a dataframe of results
    data = pd.DataFrame.from_dict(results)
    return data



def plot_random_walk(walk): 
    """ Produce a plot of the random walk generated
...     Args:
...         tuple[int, int]: Tuple of coordinates
                - x (int) : x coordinates at each point of the walk
                - y (int) : y coordinates at each point of the walk
...  """
    # Create a figure
    plt.figure()
    
    # Extract the coordinates from the walk
    x, y = walk

    # Plot the walk
    plt.plot(x, y, color = 'black')

    # Add start and end position of the random walk in different colors
    plt.plot(x[0], y[0], marker="o", color="red")
    plt.plot(x[-1], y[-1], marker = "o", color = "green")

    # edit that plot using matplotlib
    plt.title("Random walk")
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()

def plot_compare(df, num):
    """ Produce a plot of the results given in a Dataframe
...     Args:
...         df (DataFrame): The dataframe to take data from
...         num (int): Number of the experiment
...  """

    # Plot runtime against number of processors
    fig, axs = plt.subplots(nrows = 1, ncols = 2)
    fig.suptitle(f"Comparing performance with different number of processors for dataset {num}")
    axs[0].plot(df['size'], df['t_parallel'], color = 'red')
    axs[0].set_xlabel("Number of processors")
    axs[0].set_ylabel("Runtime")
    axs[0].grid(True)

    # Plot speedup against number of processors
    speedup = df['t_serial'] / df['t_parallel']
    axs[1].plot(df['size'], speedup, color = 'red')
    axs[1].set_xlabel("Number of processors")
    axs[1].set_ylabel("Speedup")
    axs[1].grid(True)
    plt.tight_layout(h_pad = 1, w_pad = 1)

    # Save the figure into a data folder
    directory_name = "data"
    
    # Create the directory
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        pass
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")

    fig.savefig(os.path.join(directory_name, f"output_{num}.png"))
    plt.show()