import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['Bookinfo', 'Hipster Shop', 'Sock Shop']
d_means = [92, 203, 487]
rd_means = [54, 137, 410]
r_means = [40, 103, 307]

e = [44, 79, 97]
bo = [d_means[0] - e[0], d_means[1] - e[1], d_means[2] - e[2]]

x = np.arange(len(labels))  # the label locations
width = 0.18  # the width of the bars
rwith = 0.16

cmap = plt.get_cmap("tab20c")
# colors = cmap(np.array([1, 5, 9]))
colors = ['#EEA140', '#2E5D95', '#8D1A10']

fig, ax = plt.subplots()
# rects1 = ax.bar(x - width, d_means, width, label='Deployment', color='black', align='edge', edgecolor='black')
# rects2 = ax.bar(x, rd_means, width, label='Re-deployment', color='white', hatch="//", align='edge', edgecolor='black')
# rects3 = ax.bar(x + width, r_means, width, label='Removal', color='white', align='edge', edgecolor='black')

rects1 = ax.bar(x - 1.5 * width, d_means, rwith, label='Deployment', color='black', align='edge', edgecolor='black')
rects2 = ax.bar(x - 0.5 * width, rd_means, rwith, label='Re-deployment', color='white', hatch="///", align='edge',
                edgecolor='black')
rects3 = ax.bar(x + 0.5 * width, r_means, rwith, label='Removal', color='white', align='edge', hatch="",
                edgecolor='black')

rects4 = ax.bar(x - 1.5 * width, e, rwith, bottom=bo, label='Policy Generation', color='white', hatch="xxxx",
                align='edge', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('processing time (ms)', fontsize=15)
# ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(fontsize=15)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=15)


if __name__ == '__main__':
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=15)
    # plt.ylim(0, 38)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    fig.set_size_inches(8, 5)
    fig.tight_layout()
    plt.savefig('bar-bench.eps', bbox_inches='tight')
    plt.show()
