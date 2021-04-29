import matplotlib.pyplot as plt
import numpy as np

d_means = [1, 6, 5, 1, 1, 1, 1, 1, 6, 5, 25, 5, 107]

d_std =   [0, 3, 2, 0, 0, 0, 0, 0, 2, 1, 7, 1, 17]

labels = ['rabbitmq', 'queue-master', 'shipping', 'payment', 'carts-db', 'catalogue-db',
          'orders-db',
          'user-db',
          'carts',
          'catalogue',
          'orders',
          'user',
          'front-end']

# If we were to simply plot pts, we'd lose most of the interesting
# details due to the outliers. So let's 'break' or 'cut-out' the y-axis
# into two portions - use the top (ax) for the outliers, and the bottom
# (ax2) for the details of the majority of our data
f, (ax, ax2) = plt.subplots(2, 1, sharex=True)

rwith = 0.5
# plot the same data on both axes
x = np.arange(len(labels))
color = '#91bfdb'
ax.bar(x, d_means, yerr=d_std, error_kw=dict(capsize=4), color=color, edgecolor='black')
ax2.bar(x, d_means, yerr=d_std, error_kw=dict(capsize=4), color=color, edgecolor='black')

ax2.set_xticks(range(13))
ax.set_yticks((100,120))
ax.tick_params(axis='y', labelsize=12)
ax2.set_xticklabels(labels, rotation=45)

# zoom-in / limit the view to different portions of the data
ax.set_ylim(89, 136)  # outliers only
ax2.set_ylim(0, 36)  # most of the data

# hide the spines between ax and ax2
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop='off')  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

# This looks pretty good, and was fairly painless, but you can get that
# cut-out diagonal lines look with just a bit more work. The important
# thing to know here is that in axes coordinates, which are always
# between 0-1, spine endpoints are at these locations (0,0), (0,1),
# (1,0), and (1,1).  Thus, we just need to put the diagonals in the
# appropriate corners of each of our axes, and so long as we use the
# right transform and disable clipping.

d = 0.01  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)  # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# What's cool about this is that now if we vary the distance between
# ax and ax2 via f.subplots_adjust(hspace=...) or plt.subplot_tool(),
# the diagonal lines will move accordingly, and stay right at the tips
# of the spines they are 'breaking'


if __name__ == '__main__':
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # ax.spines['right'].set_visible(False)
    # ax.spines['top'].set_visible(False)

    f.set_size_inches(9, 4.5)
    f.tight_layout()
    plt.savefig('bar-dis-sock.eps', bbox_inches='tight')
    plt.show()
