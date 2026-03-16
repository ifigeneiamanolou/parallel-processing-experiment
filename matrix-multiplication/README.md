# Matrix multiplication

## Comparing matrix multiplication with nested loops, numpy and multiprocessing

To explore the capabilities of the multiprocessing libraries in Python, we performed matrix multiplication in 3 different ways:
* Using 3 nested loops
* NumPy built-in matmul method
* Using a Pool of Processors and splitting the rows of the product that need to be calculated between multiple processors

## Outputs
The key outputs of the results.ipynb file are:
* A plot of runtime against number of processors
* A plot of speedup against number of processos
* Comparing parallel with numpy implementation

Further information on the project layout, along with user/developer instructions can be found on the README file of the whole project.