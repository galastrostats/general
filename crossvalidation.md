# Cross Validation

by Sheila Kannappan September 2016

This activity continues on where "Histograms, KDE, and Hypothesis Tests for Comparing Distributions" left off. We will not use cross validation on the nearest neighbor data we generated, because it is hard to create independent subsamples of companion distances, where every distance is duplicated twice. Instead we will look at u-r color distributions.

Ivezic et al. suggest that cross validation is an ideal way to choose the bandwidth for KDE (p. 254), so let's try it. Instead of leave-one-out cross validation (8.11.3), we'll use standard cross validation (8.11.1) with three subsamples: 50% of the data in a training set and 25% each in cross-validation and test sets.

Before splitting up the subsamples, determine Knuth's optimal bin size for the full sample. Also make sure your random sample division will provide similar environment distributions in all subsamples. 

Set up a regular array of bandwidths to test spanning Knuth's bin size. A geometric or "scale free" progression is preferred. For each bandwidth, determine the KDE density model with a Gaussian kernel from the training set and the summed log likelihood of the cross-validation sample assuming that model. Store the summed log likelihoods and compare across the full range, choosing the maximum log likelihood case as your preferred bandwidth. (Note: this approach is somewhat analogous to that on p. 254, but there is a typo below equation 6.5, where they wrote "minimizing" but meant "maximizing".) If you have time, you can try the supposedly optimal "epanechnikov" kernel -- what problem do you run into?

To assess the error in the KDE model with the optimized bandwidth, re-compute the KDE density model with the optimized bandwidth for both the training set and the test set. Overplot them to see the error visually. Try swapping the training set with the test+cross-validation sets and also swapping the test and cross-validation sets, and comment on the variation you see.
