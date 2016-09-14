# Bootstrapping Tutorial
by Sheila Kannappan and Rohan Isaac

## Part I: Method Analysis

Download the python code to generate Figures 3.24 and 4.3 in the book. Each of these figures uses bootstrapping, but Fig. 3.24 does not use the AstroML bootstrap function (astroML.resample.bootstrap) and instead constructs the bootstrap manually.

1. Find the source code for `astroML.resample.bootstrap` (the function used in Fig. 4.3) and explain its methodology compared to the methodology in the code for Fig. 3.24. [CAREFUL: The code uses a variable name `n_samples` that is misleading -- this variable really represents the number of data points. In fact `n_bootstraps` is the number of samples that will be drawn from the n_samples data points.] Why is it not possible to use `astroML.resample.bootstrap` in the code for Fig. 3.24?

2. The code for Fig. 3.24 contains some sloppy coding that we have encouraged you to avoid. Download and revise it to follow better coding principles. At this point you may be tempted (as your instructors were) to try to reduce the amount of looping in the code to speed it up. Why does this code require two loops for the actual bootstrap calculation although `astroML.resample.bootstrap` required only one?

## Part II: The Smoothed Bootstrap

Bootstrapping can be unreliable for small samples. Let's explore how to obtain an unbiased (or less biased) estimate of &sigma; for a small sample, using alternative forms of bootstrapping.

1. Construct an initial random sample of 5 points drawn from a Gaussian with mean = 0 and &sigma; = 1. Compare the directly computed &sigma; for this sample from `np.std` to  the input ("true") &sigma; as well as to the &sigma; found using `astroML.resample.bootstrap` with `np.std`.

2. Using the discussion in section 2 of [Hesterberg (2004)](https://github.com/galastrostats/general/blob/master/JSM04-bootknife.pdf) and modeling your code on `astroML.resample.bootstrap`, construct a utility code called `smoothedbootstrap`. Test your smoothedbootstrap code on the sample from question 1 to determine whether it performs better than the ordinary bootstrap at recovering &sigma;. For a large number of initial samples, plot the distributions or ratios of the various &sigma; estimates to compare them.

3. As time permits, construct a utility code to implement `bootknife` sampling as described in the article, and compare its performance to the smoothed bootstrap.
