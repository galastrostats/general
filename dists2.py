"""
Activity Exploring Cross-Validation
Author: Sheila Kannappan
Created: September 2016
"""

import numpy as np              # basic numerical analysis
import matplotlib.pyplot as plt # plotting
#import scipy as sp              # extended scientific function
#import scipy.stats as stats     # statistical functions
#import numpy.random as npr      # random number generation
#import astropy as ap            # core astronomy library
#import astroML as ml            # machine learning for astronomy
#import astroML.datasets as mld  # datasets
#import pymc                     # bayesian package with MCMC
import pdb                      # python debugger
#import time                     # python timekeeper
from scipy.spatial import cKDTree # see Ivezic+ p. 60
from astroML.plotting import hist # see Ivezic+ pp. 165, 225, 228
#from astroML.density_estimation import bayesian_blocks
from sklearn.neighbors import KernelDensity # see Ivezic+ pp. 251-255

"""
Start with the same data as in dists1.py
"""

data = np.genfromtxt("ECO_DR1_withradec.csv", delimiter=",", dtype=None, names=True)
name = data['NAME']
urcolor = data['MODELU_RCORR']
goodur = (urcolor > -99)

'''
In the previous activity we used Kernel Density Estimation from scikit-learn,
specifically sklearn.neighbors.KernelDensity, but we chose the bandwidth in
an ad hoc way, taking half of the Knuth histogram bin width.
'''

n0, bins0, patches0 = hist(urcolor[np.where(goodur)],bins='knuth',label='knuth',normed=1,histtype='stepfilled',color='blue',alpha=0.25)
knuthbw = (bins0[2]-bins0[1])  
bw = 0.5*knuthbw

'''
Ivezic et al. suggested that cross-validation could be a good way to 
optimize the bandwidth, so let's try it.
'''

input = np.load("crossvalidationflag.npz")
flag12 = input['flag12']

'''
Instead of leave-one-out cross-validation as described on p. 254, we'll
use regular cross-validation, with sample 1 as the training set (50% of data) 
and samples 2a and 2b as the cross-validation and test sets (25% of data each).
The likelihood cost is the sum over all points in sample 2a of the log
likelihood of the sample 2a density based on the KDE model determined
from sample 1.
'''

urdisttrain = urcolor[np.where((flag12 == 1) & goodur)]
sorttrain = np.argsort(urdisttrain)
ntrain = len(urdisttrain)
n2 = np.sum((flag12 == 2) & goodur)
nCV = int(round(0.5*n2))
urdistCV = urcolor[np.where((flag12 == 2) & goodur)][0:nCV]
urdisttest = urcolor[np.where((flag12 == 2) & goodur)][nCV:]
sortCV = np.argsort(urdistCV)
sorttest = np.argsort(urdisttest)

# want to minimize CV error = maximize likelihood of CV set given training kde
bwarr = (10**np.linspace(-0.3,0.3,10)) * knuthbw # log-spaced 0.5-5 x knuthbw
CVloglikebwarr = np.zeros(len(bwarr))
for ibw, bw in enumerate(bwarr):
    kdetrain = KernelDensity(kernel='gaussian',bandwidth=bw,rtol=1.e-12).fit(urdisttrain[:,np.newaxis])
    logdensCVcross = kdetrain.score_samples(urdistCV[:,np.newaxis])
    nottoolow = np.where(np.isfinite(logdensCVcross))
    CVloglikebwarr[ibw] = np.sum(logdensCVcross[nottoolow])
    if len(nottoolow[0]) != len(logdensCVcross):
        print "rejected %f infinities" % (nCV-len(nottoolow[0]))
bestbw = bwarr[np.where(CVloglikebwarr == max(CVloglikebwarr))]
print knuthbw, bestbw

bestbw=knuthbw
kdetrain = KernelDensity(kernel='gaussian',bandwidth=bestbw,rtol=1.e-12).fit(urdisttrain[:,np.newaxis])
logdenstrain = kdetrain.score_samples(urdisttrain[:,np.newaxis])
kdetest = KernelDensity(kernel='gaussian',bandwidth=bestbw,rtol=1.e-12).fit(urdisttest[:,np.newaxis])
logdenstest = kdetest.score_samples(urdisttest[:,np.newaxis])
plt.figure(1)
plt.clf()
plt.plot(urdisttrain[sorttrain],np.exp(logdenstrain[sorttrain]),color='blue',label='train-best')
plt.plot(urdisttest[sorttest],np.exp(logdenstest[sorttest]),color='red',label='test')
plt.xlabel("u-r color")
plt.legend(loc="best")

