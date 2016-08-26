"""
This is a template code for ASTR 503/703. It is intended to illustrate
standard imports and header information, while providing practice in
debugging, speed optimization, and spotting bad habits in programming.

Author: Sheila Kannappan
Created: August 2016
"""
import numpy as np              # basic numerical analysis
import matplotlib.pyplot as plt # plotting
import scipy as sp              # extended scientific function
import scipy.stats as stats     # statistical functions
import numpy.random as npr      # random number generation
import astropy as ap            # core astronomy library
import astroML as ml            # machine learning for astronomy
import astroML.datasets as mld  # datasets
import pymc                     # bayesian package with MCMC
import pdb                      # python debugger
import time                     # python timekeeper
# import ion()

# if any of the above does not import properly, then you need to
# revisit your package installations for anaconda

"""
Task 1: Many times a code runs fine, but the output is nonsense; you 
have to be able to debug it to figure out why. Find the errors in the 
code below, using pdb.set_trace() as described in the tutorial here: 
https://pythonconquerstheuniverse.wordpress.com/category/python-debugger/
Once you are stepping through the code line by line, check the size
and contents of the variables at each step to determine whether they
make sense.
"""

"""
Task 2: We don't always want to optimize code speed -- sometimes it's
just not important -- but you should be in the habit of avoiding 
silly things that slow your code down, like unnecessary loops. Use
time.clock() to measure the time taken by each part of the code 
below and find the rate-limiting step. Why was that step an example
of very bad coding? Next remove unnecessary loops and repeat the 
exercise to find the new rate-limiting step.
"""

"""
x=y object oriented
x/y integer
assignment of array to scalar
mismatched array lengths
function defined inside loop
single letter variables
"""

def myfunc(arrsize):
 array=np.arange(arrsize)
 return np.sqrt(array)
