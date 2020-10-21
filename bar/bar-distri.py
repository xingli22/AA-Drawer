from brokenaxes import brokenaxes
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

import pylab as pl

labels = ['cp-kafka', 'cp-zookeeper', 'cassandra', 'influxdb', 'mongodb', 'asset-management',
          'batch-operations',
          'command-delivery',
          'device-management',
          'device-registration',
          'device-state',
          'event-management',
          'event-search',
          'event-sources',
          'inbound-processing',
          'instance-management',
          'label-generation',
          'mosquitto',
          'outbound-connectors',
          'rule-processing',
          'schedule-management',
          'streaming-media',
          'web-rest']
d_means = [1, 1, 1, 1, 1, 4, 27, 23, 8, 36, 11, 26, 1, 8, 11, 8, 34, 1, 46, 11, 4, 5, 510]

d_std = [0, 0, 0, 0, 0, 0, 2, 1, 1, 2, 1, 1, 0, 0, 1, 1, 3, 0, 3, 0, 0, 1, 19]

x = np.arange(len(labels))  # the label locations
width = 0.1  # the width of the bars
rwith = 0.5

# cmap = plt.get_cmap("tab20b")
# colors = cmap(np.array([, 9, 5]))
colors = ['#f7f7f7', '#0571b0', '#92c5de']

fig = plt.figure(figsize=(8, 3))
# rects1 = ax.bar(x - width, d_means, width, label='Deployment', color='black', align='edge', edgecolor='black')
# rects2 = ax.bar(x, rd_means, width, label='Re-deployment', color='white', hatch="//", align='edge',
#                 edgecolor='black')
# rects3 = ax.bar(x + width, r_means, width, label='Removal', color='white', align='edge', edgecolor='black')

bax = brokenaxes(ylims=((0, 50), (480, 530)), left=0.25, bottom=0.25)
rwith = 0.5
rects1 = bax.bar(x - rwith * 0.5, d_means, rwith, yerr=d_std, error_kw=dict(capsize=2),
                 color=colors[0], align='edge', edgecolor='black')

# rects2 = ax2.bar(x - 1.5 * width, d_means, rwith, yerr=d_std, error_kw=dict(capsize=6), label='Deployment',
#                 color=colors[0], align='edge', edgecolor='black')

# rects4 = ax.bar(x -1.5*width, e, rwith, bottom=bo, label='Policy Generation', color='white', hatch="xxxx",align='edge', edgecolor='black')

# error = {rects1: d_std}
bax.set_ylabel('processing time (ms)', fontsize=13, labelpad=0)

# Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('time (ms)', fontsize=14)
# ax.set_title('Scores by group and gender')
# red_patch = mpatches.Patch(facecolor='white', hatch='/', label='Policy Modification', edgecolor='black')

# bax.set_xlabel(labelpad = 0)

# bax.set_xticks(x)
# bax.set_xticklabels(labels)
# bax.legend(handles=[rects1], fontsize=13)
# bax.set_ylim(450, 550)  # outliers only
# # ax2.set_ylim(0, 100)
#

if __name__ == '__main__':
    # autolabel(rects1)
    # autolabel(rects2)
    # autolabel(rects3)

    bax.xticks(fontsize=53)
    # plt.yticks(fontsize=13)
    # # plt.ylim(0,38)
    #
    # # ax.spines['right'].set_visible(False)
    # # ax.spines['top'].set_visible(False)
    #
    # # fig.set_size_inches(9, 4.5)
    # # fig.tight_layout()
    plt.savefig('bar-dis.eps')
    plt.show()
