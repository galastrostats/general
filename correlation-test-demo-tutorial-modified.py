"""
Correlation Test Demo-Tutorial
Author: Sheila Kannappan
adapted for ASTR 503/703 from CAP REU version September 2016
Modified to use loops for plotting by Rohan Isaac
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# load data
data = np.loadtxt("anscombe.txt")

# setup figure
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
labels = ['standard', 'curved', 'outlier', 'garbage']

# other common stuff
fit_x = np.array([3., 7., 11., 15., 19.])
fit_y = 3. + 0.5 * fit_x
sigmasym = r'$\sigma$'

for i, ax in enumerate(fig.axes):
    # extract x, y data
    x1, y1 = data[:, 2 * i], data[:, 2 * i + 1]

    # plot data, line
    ax.set_title(labels[i])
    ax.plot(x1, y1, 'g.', markersize=10)
    ax.plot(fit_x, fit_y, 'r', linestyle=':', linewidth=2.)

    # stats stuff
    rms = np.sqrt(np.mean((y1 - (3. + 0.5 * x1))**2))
    ax.text(3, 12, 'rms %0.2f' % rms, size=11, color='b')

    # do a some stats tests
    testn = ['Spearman rank', 'Pearson', 'Kendall Tau']
    testf = [stats.spearmanr, stats.pearsonr, stats.kendalltau]

    print("\n%s" % labels[i])
    for j, nam in enumerate(testn):
        cc, pnull = testf[j](x1, y1)
        confidence = stats.norm.interval(1. - pnull)
        leveltext = '%s %0.1f' % (nam, confidence[1])
        ax.text(8.5, 3 + 1.5 * j, leveltext + sigmasym, size=11, color='b')
        print("%s correlation coefficient %f" % (nam, cc))
        print("%s probability of no correlation %f" % (nam, pnull))

# common x, y axis
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top='off',
                bottom='off', left='off', right='off')
plt.ylabel('y-values')
plt.xlabel('x-values')

plt.show()
