import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

labels = ['200 services', '400 services', '600 services', '800 services', '1000 services']
d_means = [4064, 7866, 12062, 16063, 18968]
rd_means = [1043, 2116, 3176, 4288, 5148]
r_means = [1861, 3644, 5574, 8034, 9591]

d_std = [720.79,1139.74,1577.74,1874.74,1582.74]
rd_std = [249.79,402.74,574.74,823.74,1283.74]
r_std = [433.79,584.74,924.74,1434.74,567.74]

ten1_std = [720.79, 249.02, 433.71]
ten2_std = [1139.74, 402.82, 584.67]
ten3_std = [1577.74, 574.82, 924.67]
ten4_std = [1874.74, 823.82, 1434.67]
ten5_std = [2955.74, 1957.82, 7751.67]


e = [899, 1559, 2417, 3030, 3721]
bo = [d_means[0] - e[0], d_means[1] - e[1], d_means[2] - e[2], d_means[3] - e[3], d_means[4] - e[4]]

x = np.arange(len(labels))  # the label locations
width = 0.28  # the width of the bars
rwith = 0.28

# cmap = plt.get_cmap("tab20b")
# colors = cmap(np.array([, 9, 5]))
colors = ['#f7f7f7', '#0571b0', '#92c5de']


fig, ax = plt.subplots()
# rects1 = ax.bar(x - width, d_means, width, label='Deployment', color='black', align='edge', edgecolor='black')
# rects2 = ax.bar(x, rd_means, width, label='Re-deployment', color='white', hatch="//", align='edge',
#                 edgecolor='black')
# rects3 = ax.bar(x + width, r_means, width, label='Removal', color='white', align='edge', edgecolor='black')

rects1 = ax.bar(x - 1.5 * width, d_means, rwith, yerr=d_std,error_kw=dict(capsize=6), label='Deployment', color=colors[0], align='edge', edgecolor='black')
rects2 = ax.bar(x - 0.5 * width, rd_means, rwith, yerr=rd_std,error_kw=dict(capsize=6), label='Re-deployment', color=colors[1], align='edge',
                edgecolor='black')
rects3 = ax.bar(x + 0.5 * width, r_means, rwith, yerr=r_std,error_kw=dict(capsize=6), label='Removal', color=colors[2], align='edge', hatch="",
                edgecolor='black')


# rects4 = ax.bar(x -1.5*width, e, rwith, bottom=bo, label='Policy Generation', color='white', hatch="xxxx",align='edge', edgecolor='black')

error = {rects1: d_std, rects2: rd_std, rects3: r_std}
ax.set_ylabel('processing time (ms)', fontsize=13)

# Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('time (ms)', fontsize=14)
# ax.set_title('Scores by group and gender')
red_patch = mpatches.Patch(facecolor='white', hatch = '/',label='Policy Modification', edgecolor='black')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(handles=[rects1, rects2,rects3, red_patch],fontsize=13)


patterns_2 = ('/', '/', '/', '/', '/')
for bar, pattern in zip(rects1, patterns_2):
    bar.set_hatch(pattern)




def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    i=0
    for rect in rects:
        xx = 3
        if rect.get_height() == 1724:
            xx = 8
        if rect.get_height() == 1406:
            xx = 2
        height = rect.get_height()
        ax.annotate('{:,}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 1.6, height+error[rects][i]),
                    xytext=(0, xx),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=12)
        i=i+1

if __name__ == '__main__':
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    # plt.ylim(0,38)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    fig.set_size_inches(9, 4.5)
    fig.tight_layout()
    plt.savefig('bar-large.eps', bbox_inches='tight')
    plt.show()
