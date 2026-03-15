# Comparing serial and parallel implementation of computation-heavy tasks

This project aims to investigate the power of using processes to perform CPU-heavy respectively. It focuses on two main tasks:

1) Matrix multiplication
2) Monte carlo simulation

## Introduction
Both of the above sub-projects are divided in 3 main parts:

1) Serial and parallel implementation of CPU heavy task
2) Benchmarking runtime and calculation of speedup
3) Evaluation of the results using graphs, focusing on the limitations of scaling due to memory overhead (these results can be found in the corresponding .ipynb files)

Each sub-project has its own folder and README.md file.

## User/Developer Instructions
To compile and run the jupyter files, you need to follow these steps:
1) Clone the repository

git clone https://github.com/ifigeneiamanolou/parallel-processing-experiment.git

2) Create a python virtual environment "myenv"

python3.13 -m venv myenv

Activate it using 

myenv\Scripts\activate

for Windows and 

source myenv/bin/activate 

for MacOS

3) Install dependancies

pip install -r requirements.txt

4) Run the jupyter notebooks using "Run all"