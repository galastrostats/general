'''
ASTR 503/703 Midterm Challenge
October 2016
This take-home test is intended to be completed in 3 hours. Please do not spend 
more than 5 hours on it. If a blank region is 3+ spaces long, you are expected
to fill in code. If it's only one space, then a text comment is all you need.
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from astroML.utils import check_random_state

# you are given a file of input data xx and yy; the uncertainties are unknown

# load the data and plot it

input = np.load('xydata.npz')
xx = input['xx']
yy = input['yy']




# determine whether there is a correlation using both the Pearson & the
# Spearman Rank tests and print out the probability that there *is* a 
# correlation expressed as a number between 0-100%



# check whether your results are invariant under swapping xx and yy
# since you do not know the relative error in xx and yy



# select the preferred frequentist linear fit between the forward, inverse, 
# and bisector fits, plot it, and print out its coefficients (slope and 
# intercept expressed assuming yy = slope*xx + intercept)



# use bootstrap resampling of the data to determine the 68% confidence
# intervals for the slope and intercept you computed above
# (hint: you cannot use the pre-made bootstrap/smoothedbootstrap functions
# but must construct a custom bootstrap as Ivezic Fig. 3.24 had to do)

nboot=100
Ndata=len(xx)
sloperesults = np.zeros(nboot)
intresults = np.zeros(nboot)
random_state=None
rng = check_random_state(random_state)
ind = rng.randint(Ndata, size=(Ndata,nboot))
#for k in range(nboot):



#slopesort=np.argsort(sloperesults)
#intsort=np.argsort(intresults)

#print "68%% confidence interval for slope: %0.2f -- %0.2f" % (,)
#print "68%% confidence interval for intercept: %0.2f -- %0.2f" % (,)

# now suppose we wish to determine whether a 2nd order model is
# superior to a 1st order one for this data set -- this problem is too
# hard for a 3-hour test if we allow for errors in both variables, so
# we'll assume from now on that all the scatter is in the yy direction

# perform 1st and 2nd order polyfit results



# compute the reduced chi^2 to compare the fits: here please note that
# since you don't know the error bars, you'll have to assume some value
# for them -- you can't estimate them from the rms around the fit as
# that would give a different answer for the 1st and 2nd order fits,
# biasing the comparison -- so let's first assume error bars = 2.
errs = 2.



#print "reduced chi^2 for 1st order fit = %0.2f and for 2nd order fit = %0.2f" % (redchisq1,redchisq2)

# what is wrong with the reduced chi^2 values? adjust your error bar assumption to fix the problem

# plot the two fits



# which fit order is preferred based on this analysis? does your preferred
# fit shed any light on why the Spearman rank test yielded lower confidence
# in a correlation than the Pearson test?

# use stats.chi2.ppf to determine whether the fit order you did not
# prefer is rejected at >68% or >95% one-sided confidence, i.e., "one
# sigma" or "two sigma" confidence in the language of Gaussians
# (watch out that ppf returns chi^2, not reduced chi^2)




# how confident are you in your choice of fit order? explain

'''
side note: if we had wanted to assume a mix of error in xx and error in yy,
we could have used scipy.odr (orthogonal distance regression) which supports
polynomial fitting and user-supplied functions -- for details see
http://docs.scipy.org/doc/scipy/reference/odr.html and
http://blog.rtwilson.com/orthogonal-distance-regression-in-python/
'''

# below is a code block you can uncomment with two Bayesian likelihood grid 
# calculations for the 1st and 2nd order model parameters, assuming flat priors

'''
ndata=len(xx)
nalpha=100
nbeta=100
alphaposs = np.linspace(pfit1[0]-4.*np.sqrt(covp1[0,0]),pfit1[0]+4.*np.sqrt(covp1[0,0]),nalpha)
betaposs = np.linspace(pfit1[1]-4.*np.sqrt(covp1[1,1]),pfit1[1]+4.*np.sqrt(covp1[1,1]),nbeta)
prior=1.
modelgridterm1 = alphaposs.reshape(1,nalpha) * xx.reshape(ndata,1) 
modelgrid = modelgridterm1.reshape(ndata,nalpha,1) + betaposs.reshape(nbeta,1,1).T
residgrid = yy.reshape(ndata,1,1) - modelgrid
chisqgrid = np.sum(residgrid**2/errs**2,axis=0)        
lnpostprob1 = (-1./2.)*chisqgrid + np.log(prior) 

ndata=len(xx)
np0=100
np1=100
np2=100
p0poss = np.linspace(pfit2[0]-4.*np.sqrt(covp2[0,0]),pfit2[0]+4.*np.sqrt(covp2[0,0]),np0)
p1poss = np.linspace(pfit2[1]-4.*np.sqrt(covp2[1,1]),pfit2[1]+4.*np.sqrt(covp2[1,1]),np1)
p2poss = np.linspace(pfit2[2]-4.*np.sqrt(covp2[2,2]),pfit2[2]+4.*np.sqrt(covp2[2,2]),np2)
prior=1.
modelgridterm1 = p0poss.reshape(1,np0) * xx.reshape(ndata,1)
modelgridterm2 = modelgridterm1.reshape(ndata,np0,1) + p1poss.reshape(np1,1,1).T
modelgrid = modelgridterm2.reshape(ndata,np0,np1,1) + p2poss.reshape(np2,1,1,1).T
residgrid = yy.reshape(ndata,1,1,1) - modelgrid
chisqgrid = np.sum(residgrid**2/errs**2,axis=0)        
lnpostprob2 = (-1./2.)*chisqgrid + np.log(prior) 
'''

# marginalize over all parameters in the two posterior distributions to
# decide whether a Bayesian odds calculation favors a 1st or 2nd order model




#print "odds favoring a 1st order over a 2nd order model: %0.2f" % odds

# consult Ivezic section 5.4 -- does your result agree with your earlier result
# based on chi^2 analysis? discuss the confidence levels in each analysis
