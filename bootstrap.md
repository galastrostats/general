# Bootstrapping Tutorial
by Sheila Kannappan and Rohan Isaac

## Part I: Method Analysis

Download the python code to generate Figures 3.24 and 4.3 in the book. Each of these figures uses bootstrapping, but Fig. 3.24 does not use the AstroML bootstrap function (astroML.resample.bootstrap) and instead constructs the bootstrap manually.

1. Find the source code for `astroML.resample.bootstrap` (the function used in Fig. 4.3) and explain its methodology compared to the methodology in the code for Fig. 3.24. [CAREFUL: The code uses a variable name `n_samples` that is misleading -- this variable really represents the number of data points. In fact `n_bootstraps` is the number of samples that will be drawn from the n_samples data points.] Why is it not possible to use `astroML.resample.bootstrap` in the code for Fig. 3.24?

2. The code for Fig. 3.24 contains some sloppy coding that we have encouraged you to avoid. Download and revise it to follow better coding principles. At this point you may be tempted (as your instructors were) to try to reduce the amount of looping in the code to speed it up. Why does this code require two loops for the actual bootstrap calculation although `astroML.resample.bootstrap` required only one?
