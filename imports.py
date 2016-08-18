import numpy as np		# basic numerical analysis
import matplotlib.pyplot as plt	# plotting
import scipy as sp		# extened scientific function
import scipy.stats as stats	# statistical functions
import numpy.random as npr	# random number generation
import astropy as ap		# core astronomy library
import astroML as ml		# machine learning for astronomy
import astroML.datasets as mld 	# datasets
import pymc			# bayesian methods including markov chain monte carlo
#plt.ion()

x = np.random.random(2000)
y = np.random.random(2000)
z = np.sin(x)*np.sin(y)
plt.plot(x,y)
plt.show()
