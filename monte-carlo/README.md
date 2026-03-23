# Performing a monte carlo simulation for multiple random walks using parallel processors

## What is a Monte-Carlo simulation
A mMonte-Carlo simulation is a method to understand how systems behave under uncertainty. It works by running multiple experiments with random inputs and then evaluating the possible outcomes and their respective probabilities. In other words, it uses random samples to estimate the expected value of a function f over a domain D (set of random samples). It has multiple real-world applications including:

* Calculation of pi
* Optimization of hyperparameters in neural networks
* Uncertainty estimation for AI models
* Risk assessment in financial models
* Random walks


## What are random walks
In this project, we will focus on random walks. A random walk is a path formed by a sequence of random steps taken in 1-D, 2-D and so on. We will simulate this, by randomly picking from a list of possible steps multiple times and visualizing the path using matplotlib. Random walks are used for example to:

1. Simulate the movement of gas or liquid molecules
2. Showcase stock market trends
3. Describe the statistical properties of a genetic drift
4. Model neuron behavior in the human brain.

## Focus of this project
We will simulate a 2D random walk, where the walker has 4 possible options for its step each time (up, down, left or right). We will run this simulation multiple times on multiple parallel processors, as well as serially, to compare runtime between serial and parallel implentation and calculate speedup, to determine the optimal number of parallel processors. Then, using all of those simulations we can derive useful statistics from the simulations.

## How parallel processing can be applied to random walks
Parallel processing can be used in Monte-Carlo simulations of random walks by distributiing the workload (large number of independant random walks) between multiple processors. Since this is a CPU-heavy task, we used ProcessPoolExecutor, which is a subclass of Executor, from the Python library concurrent.futures. In essense, it employs a pool of processors to execute calls to functions asychronously.

## Outputs
The key outputs of the results.ipynb file are:
* A plot of runtime against number of processors
* A plot of speedup against number of processos
* Mean ending position of the random walk
* Standard deviation of the ending position of the walk
* Distribution plot of the ending position

Further information on the project layout, along with user/developer instructions can be found on the README file of the whole project.

