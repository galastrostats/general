"""
Activity Exploring Histograms, KDE, and Hypothesis Tests for Comparing Distributions
Author: Sheila Kannappan
Created: September 2016
"""

import numpy as np              # basic numerical analysis
import matplotlib.pyplot as plt # plotting
#import scipy as sp              # extended scientific function
import scipy.stats as stats     # statistical functions
import numpy.random as npr      # random number generation
#import astropy as ap            # core astronomy library
#import astroML as ml            # machine learning for astronomy
#import astroML.datasets as mld  # datasets
#import pymc                     # bayesian package with MCMC
#import pdb                      # python debugger
#import time                     # python timekeeper
from scipy.spatial import cKDTree # see Ivezic+ p. 60
from astroML.plotting import hist # see Ivezic+ pp. 165, 225, 228
#from astroML.density_estimation import bayesian_blocks
from sklearn.neighbors import KernelDensity # see Ivezic+ pp. 251-255

"""
Let's explore galaxy properties in relation to neighbor proximity using ECO.
We'll use the input file "ECO_DR1_withradec.csv" which contains these columns:
'NAME', 'RADEG', 'DEDEG', 'CZ', 'LOGMSTAR', 'MODELU_RCORR', 'R90', 'MORPHEL',
'GRPCZ', 'FC', 'LOGMH', 'DEN1MPC'.
"""

data = np.genfromtxt("ECO_DR1_withradec.csv", delimiter=",", dtype=None, names=True)
name = data['NAME']
radeg = data['RADEG']
decdeg = data['DEDEG']
grpcz = data['GRPCZ']
cz = data['CZ']

# convert RA Dec coordinates to physical units
# using simple Hubble Law distances because staying in local universe,
# so error from ignoring cosmology is small
H0=70. # km/s/Mpc
Z_Mpc = cz / H0 # using cz includes peculiar motions
X_Mpc = 2.*np.pi * Z_Mpc * radeg * np.cos(np.pi*decdeg/180.) / 360.
Y_Mpc = 2.*np.pi * Z_Mpc * decdeg / 360.
Z_Mpcnopec = grpcz / H0 # using grpcz sets DeltaZ=0 within a group
X_Mpcnopec = 2.*np.pi * Z_Mpcnopec * radeg * np.cos(np.pi*decdeg/180.) / 360.
Y_Mpcnopec = 2.*np.pi * Z_Mpcnopec * decdeg / 360.

# find 3D neighbors with Z_Mpc
coords = np.array([X_Mpc, Y_Mpc, Z_Mpc]).T
kdt = cKDTree(coords)
neighbordist, neighbori = kdt.query(coords, k=2)
neighbordist = neighbordist[:,1] # ignore self-match
neighbori = neighbori[:,1] # ignore self-match

# find 3D neighbors with Z_Mpcnopec
coordsnopec = np.array([X_Mpcnopec, Y_Mpcnopec, Z_Mpcnopec]).T
kdtnopec = cKDTree(coordsnopec)
neighbordistnopec, neighborinopec = kdtnopec.query(coordsnopec, k=2)
neighbordistnopec = neighbordistnopec[:,1] # ignore self-match
neighborinopec = neighborinopec[:,1] # ignore self-match

# plot histograms of distances with optimal binning
plt.figure(1)
plt.clf()
#hist(neighbordist,bins='freedman',label='freedman',normed=1,histtype='stepfilled',color='green',alpha=0.5)
#hist(neighbordist,bins='scott',label='scott',normed=1,histtype='step',color='purple',alpha=0.5,hatch='///')
hist(neighbordist,bins='knuth',label='knuth',normed=1,histtype='stepfilled',color='blue',alpha=0.25)
plt.xlim(0,6)
plt.xlabel("dist (Mpc)")
plt.title("Allowing peculiar motions, false Delta Z-dist within groups")
plt.legend(loc="best")

plt.figure(2)
plt.clf()
#hist(neighbordistnopec,bins='freedman',label='freedman',normed=1,histtype='stepfilled',color='green',alpha=0.5)
#hist(neighbordistnopec,bins='scott',label='scott',normed=1,histtype='step',color='purple',alpha=0.5,hatch='///')
n0, bins0, patches0 = hist(neighbordistnopec,bins='knuth',label='knuth',normed=1,histtype='stepfilled',color='blue',alpha=0.25)
plt.xlim(0,6)
plt.xlabel("dist (Mpc)")
plt.title("No peculiar motions, zero Delta Z-dist within groups")
plt.legend(loc="best")

# Comparing with Fig. 5.20 (p. 277), Scott's rule seems to make
# overly fat bins for our Fig. 2, as in their example, but it
# appears better than the Freedman-Diaconis rule for our Fig. 1,
# where the Freedman-Diaconis rule gives a "noisy" histogram.

# For comparison, try variable optimized bin widths (Bayesian blocks). 
plt.figure(1)
#neighbordist = neighbordist + npr.normal(0.0, 0.03, len(neighbordist))
n1, bins1, patches1 = hist(neighbordist,bins='blocks',label='blocks',normed=1,histtype='step',color='red',hatch="\\\ ")
plt.legend(loc="best")

plt.figure(2)
#neighbordistnopec = neighbordistnopec + npr.normal(0.0, 0.03, len(neighbordistnopec))
n2, bins2, patches2 = hist(neighbordistnopec,bins='blocks',label='blocks',normed=1,histtype='step',color='red',hatch="\\\ ")
plt.legend(loc="best")

# To find out what bins the Bayesian blocks algorithm found, echo back:
for i in xrange(len(bins2)): print "%0.4f" % bins2[i]
# Looks like we can consider anything beyond this distance as fairly isolated:
distcut = 0.31

# The spikes in the Bayesian blocks histogram are a bit annoying -- we could
# play with the prior to disfavor small intervals, but maybe it would be more
# entertaining to give Kernel Density Estimation a try. KDE is shown in Ivezic+ 
# Fig. 6.1 but we'll use this newer version: sklearn.neighbors.KernelDensity -- see
# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html

bw = 0.5*(bins0[2]-bins0[1]) 
# initially using 0.5*Knuth binsize as bandwidth; should test other values
kde = KernelDensity(kernel='epanechnikov',bandwidth=bw).fit(neighbordist[:,np.newaxis])
kdenopec = KernelDensity(kernel='epanechnikov',bandwidth=bw).fit(neighbordistnopec[:,np.newaxis])
xx = np.linspace(-2,16,10000)[:,np.newaxis]
logdens = kde.score_samples(xx)
logdensnopec = kdenopec.score_samples(xx)
print "TOTAL INTEGRAL %f" % (np.sum(0.0018*np.exp(logdensnopec)))
plt.figure(1)
plt.plot(xx,np.exp(logdens),color='green',label='kde')
plt.legend(loc="best")
plt.figure(2)
plt.plot(xx,np.exp(logdensnopec),color='green',label='kde')
plt.legend(loc="best")

# This looks great, although now the bandwidth has taken the place of the bin
# width as the mysterious quantity we must somehow optimize. Ivezic+ p. 254
# suggests cross-validation as a way to find the best bandwidth -- we'll look
# at cross-validation more later, but for now we'll just say it involves subdividing
# the sample to calibrate the result with different subsamples.

# In general, subdividing the sample is always a great idea for testing 
# distributions. For example, there appears to be an exclusion zone in the
# neighbor distances KDE plot for distances < 0.06 Mpc. To see if this exclusion
# zone is real, let's see if it shows up for two separate regions of the sky.

# Compare neighbor distance distributions in the north vs. south
innorth = (decdeg > 15.)
selenvnorth = np.where(innorth)
selenvsouth = np.where(~innorth)

plt.figure(3)
plt.clf()
hist(neighbordistnopec[selenvnorth],bins='knuth',label='north',normed=1,histtype='stepfilled',color='red',alpha=0.25)
plt.xlim(0,6)
kde = KernelDensity(kernel='epanechnikov',bandwidth=bw).fit(neighbordistnopec[selenvnorth][:,np.newaxis])
logdens = kde.score_samples(xx)
plt.plot(xx,np.exp(logdens),'r--')
hist(neighbordistnopec[selenvsouth],bins='knuth',label='south',normed=1,histtype='stepfilled',color='blue',alpha=0.25)
kde = KernelDensity(kernel='epanechnikov',bandwidth=bw).fit(neighbordistnopec[selenvsouth][:,np.newaxis])
logdens = kde.score_samples(xx)
plt.plot(xx,np.exp(logdens),'b--')
DD, pnullks = stats.ks_2samp(neighbordistnopec[selenvnorth],neighbordistnopec[selenvsouth])
UU, pnullmw = stats.mannwhitneyu(neighbordistnopec[selenvnorth],neighbordistnopec[selenvsouth])
plt.text(1, 2, "K-S pnull = %0.2g" % pnullks, size=14, color='b')
plt.text(1, 1.7, "M-W pnull = %0.2g" % pnullmw, size=14, color='b')
plt.xlabel("nearest neighbor dists (Mpc)")
plt.legend()

# Yikes! The exclusion zone seems real, but these two samples are not drawn from
# the same parent distribution! You're witnessing cosmic variance. In the presence
# of cosmic variance, we would like much larger survey volumes to average out 
# such differences. However, for some purposes it may work to divide the sample
# randomly. Let's do this in preparation for learning about cross-validation.

makenew = False
if makenew:
    #pdb.set_trace()
    sample2inds = npr.choice(len(name),size=int(round(0.5*len(name)-1)),replace=False)
    flag12 = np.zeros(len(name),dtype=int)
    flag12[sample2inds] = 1
    flag12 += 1
else:
    input = np.load("crossvalidationflag.npz")
    flag12 = input['flag12']
sample1inds = np.where(flag12 == 1)
sample2inds = np.where(flag12 == 2)

plt.figure(4)
plt.clf()
n, bins, patches = hist(neighbordistnopec[sample1inds],bins='knuth',label='1',histtype='stepfilled',color='red',alpha=0.25)
hist(neighbordistnopec[sample2inds],bins=bins,label='2',histtype='stepfilled',color='blue',alpha=0.25)
plt.xlim(0,6)
DD, pnullks = stats.ks_2samp(neighbordistnopec[sample1inds],neighbordistnopec[sample2inds])
plt.text(2, 200, "K-S pnull = %0.2g" % pnullks, size=14, color='b')
plt.xlabel("nearest neighbor dists (Mpc)")
plt.legend()

print "cmp fracts: [1] %0.3f  [2] %0.3f" % (np.sum((flag12 == 1) & (neighbordistnopec < distcut))/np.float(np.sum(flag12 == 1)),np.sum((flag12 == 2) & (neighbordistnopec < distcut))/np.float(np.sum(flag12 == 2)))

# Sample 1 will be our training set, and we will subdivide Sample 2 to provide
# our cross-validation and test sets; since these samples change each time we re-run,
# we can save our favorite randomization in an npz file
#np.savez('crossvalidationflag',flag12=flag12)

