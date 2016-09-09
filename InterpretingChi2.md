The 2 test involves computing the 2 value, which is useful for determining whether a model is consistent with a data set within its errors. Most (astro)physicists define it as  where Oi, Ei , and i are the Observed and Expected values and the errors. In other words, the numerator represents the actual residuals between the data and the model, and the denominator represents the expected residuals assuming Gaussian-distributed errors. (Note however that in statistics, 2 is generally defined with an Ei in the denominator, which represents the special case of Poisson-distributed data. If this distribution is unfamiliar to you, don’t worry about it.) 

To see how the 2 value can serve as a test, consider that if the model is correct and the errors have been correctly estimated, 2 ≈ N, where N is the number of degrees of freedom (number of data points minus number of parameters in the model). Therefore scientists often speak loosely and say that if the “reduced” Chi-squared defined as 2/N is approximately equal to 1, then the fit is good. But let’s take a closer look.

(a) Using Monte Carlo methods, create 1000 fake data sets following the underlying functional form y=1/x for x = 1, 2, 3…30 with Gaussian random errors on y of amplitude 0.1. Each data set defines one value of 2, and the 1000 values of 2 from all of the data sets can be divided by N and binned into a histogram to show you the reduced 2 distribution, which is a well-defined function analogous to a Gaussian or any other function. Note that y=1/x has no free parameters, so N is just the # of data points, 30.

(b) Now create 1000 fake data sets each with 300 values of x = 1.1, 1.2, 1.3… 30.9, using the same function y=1/x with the same errors of 0.1 on y. Overplot the new histogram of reduced 2 values for N=300. Is a reduced 2 of 1.3 equally good for both data sets?

(c) Use a K-S test (stats.ks_2samp) to quantify your confidence level that the two 2 distributions are different. Google the functional form of the 2 distribution on the web to understand why in mathematical terms.

(d) This exercise shows that just knowing that the reduced 2 ≈ 1 does not tell you how good your model is. You must know N. If you do, you can compute confidence levels by integrating the probability under the normalized 2 distribution up to your measured 2. Use np.argsort to do this approximately with the 2 distributions from your Monte Carlo.

(e) Again, analyze the code used to create the plots in this exercise. What helpful data display strategies have been employed?

Advanced Topics. When comparing models, you can use the fact that the probability or “likelihood” L that a given model is correct is proportional to  , and the likelihood ratio L1 /L2  formed with two different 2 values from two different models describes our confidence in one model relative to the other. Such comparisons form the basis of Bayesian statistics. Google “likelihood ratio test” or “Bayesian statistics” to learn more.
 
