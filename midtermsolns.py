'''
ASTR 503/703 Midterm Challenge
October 2016
This take-home test is intended to be completed in 3 hours. Please do not spend more than
5 hours on it.
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from astroML.utils import check_random_state

def bisectorslope(fsl,isl):
    # function to compute bisector slope from forward and inverse slopes
    # using formula in Isobe et al (1990)
    bsl1 = (1./(fsl+isl))
    bsl2 = (fsl*isl - 1. + np.sqrt((1.+fsl**2)*(1.+isl**2)))
    bsl = bsl1*bsl2
    return bsl

# you are given a file of input data xx and yy; the uncertainties are unknown

# load the data and plot it

input = np.load('xydata.npz')
xx = input['xx']
yy = input['yy']

plt.figure(1)
plt.clf()
plt.plot(xx,yy,'b.')

# determine whether there is a correlation using both the Pearson & the
# Spearman Rank tests and print out the probability that there *is* a 
# correlation expressed as a number between 0-100%

ccp, pnullp = stats.pearsonr(xx,yy)
ccs, pnulls = stats.spearmanr(xx,yy)

print "Pearson prob. of correlation = %0.1f" % (100.*(1-pnullp))
print "Spearman rank prob. of correlation = %0.1f" % (100.*(1-pnulls))

# check whether your results are invariant under swapping xx and yy
# since you do not know the relative error in xx and yy

ccpi, pnullpi = stats.pearsonr(yy,xx)
ccsi, pnullsi = stats.spearmanr(yy,xx)

print "Pearson prob. of inverse correlation = %0.1f" % (100.*(1-pnullpi))
print "Spearman rank prob. of inverse correlation = %0.1f" % (100.*(1-pnullsi))

# select the preferred frequentist linear fit between the forward, inverse, 
# and bisector fits, plot it, and print out its coefficients (slope and 
# intercept expressed assuming yy = slope*xx + intercept)

# bisector preferred
pforward = np.polyfit(xx,yy,1)
slopefor = pforward[0]
intfor = pforward[1]
pinverse = np.polyfit(yy,xx,1)
slopeinv = 1./pinverse[0]
intinv = -1.*pinverse[1]/pinverse[0]
slopebis = bisectorslope(slopefor,slopeinv)
intbis = np.mean(yy) - slopebis*np.mean(xx)

xtoplot = np.linspace(2,16,10)
plt.plot(xtoplot,slopebis*xtoplot+intbis,'r')
print "fit slope = %0.2f and intercept = %0.2f" % (slopebis,intbis)

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
for k in range(nboot):
    pforward = np.polyfit(xx[ind[:,k]], yy[ind[:,k]],1)
    slopefor = pforward[0]
    intfor = pforward[1]
    pinverse = np.polyfit(yy[ind[:,k]], xx[ind[:,k]],1)
    slopeinv = 1./pinverse[0]
    intinv = -1.*pinverse[1]/pinverse[0]
    sloperesults[k] = bisectorslope(slopefor,slopeinv)
    intresults[k] = np.mean(yy) - sloperesults[k]*np.mean(xx)
slopesort=np.argsort(sloperesults)
intsort=np.argsort(intresults)

print "68%% confidence interval for slope: %0.2f -- %0.2f" % (sloperesults[slopesort[16]],sloperesults[slopesort[84]])
print "68%% confidence interval for intercept: %0.2f -- %0.2f" % (intresults[intsort[16]],intresults[intsort[84]])

# now suppose we wish to determine whether a 2nd order model is
# superior to a 1st order one for this data set -- this problem is too
# hard for a 3-hour test if we allow for errors in both variables, so
# we'll assume from now on that all the scatter is in the yy direction

# perform 1st and 2nd order polyfit results

pfit1, covp1 = np.polyfit(xx, yy, 1, cov='True')
pfit2, covp2 = np.polyfit(xx, yy, 2, cov='True')

# compute the reduced chi^2 to compare the fits

# note that since you don't know the error bars, you'll have to assume
# some value for them -- you can't estimate them from the rms around the fit
# as that would give a different answer for the 1st and 2nd order fits,
# biasing the comparison

# first assume error bars = 2. -- what is wrong with the reduced chi^2
# values? adjust your error bar assumption to fix the problem

# the reduced chi^2 was too small -- change 2. to 1.65 to match rms
errs = 1.65
print "rms1 %0.2f" % np.sqrt(np.mean((yy - np.polyval(pfit1, xx))**2))
print "rms2 %0.2f" % np.sqrt(np.mean((yy - np.polyval(pfit2, xx))**2))
redchisq1 = np.sum((yy - np.polyval(pfit1, xx))**2) / errs**2 / (len(xx)-2)
redchisq2 = np.sum((yy - np.polyval(pfit2, xx))**2) / errs**2 / (len(xx)-3)
print "reduced chi^2 for 1st order fit = %0.2f and for 2nd order fit = %0.2f" % (redchisq1,redchisq2)

# plot the two fits
plt.plot(xtoplot,np.polyval(pfit1,xtoplot),'b')
plt.plot(xtoplot,np.polyval(pfit2,xtoplot),'g')

# which fit order is preferred based on this analysis? does your preferred
# fit shed any light on why the Spearman rank test yielded lower confidence
# in a correlation than the Pearson test?

# the 2nd order fit is favored slightly -- if correct, this would imply that
# the data curve back down, violating the monotonicity requirement of 
# Spearman rank and thus explaining its weaker correlation significance

# use stats.chi2.ppf to determine whether the fit order you did not
# prefer is rejected at >68% or >95% one-sided confidence, i.e., "one
# sigma" or "two sigma" confidence in the language of Gaussians
# (watch out that ppf returns chi^2, not reduced chi^2)

print stats.chi2.ppf(0.68, len(xx)-2) / (len(xx)-2)
print stats.chi2.ppf(0.95, len(xx)-2) / (len(xx)-2)

# how confident are you in your choice of fit order?
# not even 2sigma confident, the chi^2 test only mildly favors 2nd order

'''
side note: if we had wanted to assume a mix of error in xx and error in yy,
we could have used scipy.odr (orthogonal distance regression) which supports
polynomial fitting and user-supplied functions -- for details see
http://docs.scipy.org/doc/scipy/reference/odr.html and
http://blog.rtwilson.com/orthogonal-distance-regression-in-python/
'''

# below is a code block you can uncomment with two Bayesian likelihood grid 
# calculations for the 1st and 2nd order model parameters, assuming flat priors

#'''
ndata=len(xx)
nalpha=100
nbeta=100
alphaposs = np.linspace(pfit1[0]-4.*np.sqrt(covp1[0,0]),pfit1[0]+4.*np.sqrt(covp1[0,0]),nalpha)
betaposs = np.linspace(pfit1[1]-4.*np.sqrt(covp1[1,1]),pfit1[1]+4.*np.sqrt(covp1[1,1]),nbeta)
prior=1. # better to write 1./(8.*np.sqrt(covp1[0,0])* 8.*np.sqrt(covp1[1,1]))
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
prior=1. # better to write 1./(8.*np.sqrt(covp2[0,0])* 8.*np.sqrt(covp2[1,1]) * 8.*np.sqrt(covp2[2,2]))
modelgridterm1 = p0poss.reshape(1,np0) * xx.reshape(ndata,1)**2
modelgridterm2 = modelgridterm1.reshape(ndata,np0,1) + (p1poss.reshape(np1,1,1).T * xx.reshape(ndata,1,1))
modelgrid = modelgridterm2.reshape(ndata,np0,np1,1) + p2poss.reshape(np2,1,1,1).T
residgrid = yy.reshape(ndata,1,1,1) - modelgrid
chisqgrid = np.sum(residgrid**2/errs**2,axis=0)        
lnpostprob2 = (-1./2.)*chisqgrid + np.log(prior) 
#'''

# marginalize over all parameters in the two posterior distributions to
# decide whether the Bayesian odds favors a 1st or 2nd order model

# note that the "implicit" prior set by the allowed parameter ranges
# matters now (see "Occam's Razor" in Ivezic 5.4.2)
postprob1=np.exp(lnpostprob1) * 1./(8.*np.sqrt(covp1[0,0])* 8.*np.sqrt(covp1[1,1]))
postprob2=np.exp(lnpostprob2) * 1./(8.*np.sqrt(covp2[0,0])* 8.*np.sqrt(covp2[1,1]) * 8.*np.sqrt(covp2[2,2]))
odds = np.sum(postprob1) / np.sum(postprob2)

print "odds favoring a 1st order over a 2nd order model: %0.2f" % odds

# consult Ivezic section 5.4 -- does your result agree with your earlier result
# based on chi^2 analysis? discuss the confidence levels in each analysis

# the 1st order is disfavored at <2sigma confidence by the frequentist 
# analysis, whereas it is much more strongly disfavored by the Bayesian
# analysis (factor >10 = "strong" evidence per section 5.4)