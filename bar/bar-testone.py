import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

labels = ['Deploy New Version', 'Remove Old Version']
nai_means = [72, 31]


nai_std = [11.69, 2.86]

x = np.arange(len(labels))  # the label locations

print(x)
width = 0.3  # the width of the bars
rwidth = 0.16

cmap = plt.get_cmap("tab20c")
# colors = cmap(np.array([1, 5, 9]))
colors = ['#ef8a62', '#67a9cf', '#91bfdb']

# f7f7f7


fig, ax = plt.subplots()
# rects1 = ax.bar(x - width, d_means, width, label='Deployment', color='black', align='edge', edgecolor='black')
# rects2 = ax.bar(x, rd_means, width, label='Re-deployment', color='white', hatch="//", align='edge', edgecolor='black')
# rects3 = ax.bar(x + width, r_means, width, label='Removal', color='white', align='edge', edgecolor='black')

rects1 = ax.bar(x-width/2, nai_means, width, yerr=nai_std, error_kw=dict(capsize=6), label='Baseline',
                color=colors[1], align='edge', edgecolor='black')
# rects2 = ax.bar(x + 0.01, opt_means, width, yerr=opt_std, error_kw=dict(capsize=6), label='AutoArmor', color=colors[1],
#                 align='edge',
#                 edgecolor='black')

error = {rects1: nai_std}

red_patch = mpatches.Patch(facecolor='white', hatch='/', label='Policy Modification', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('processing time (ms)', fontsize=16)
# ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.grid(axis='y')
# ax.legend(handles=[rects1], fontsize=16)
# ax.legend(fontsize=15)


# patterns_1 = ('/', '/', '/')
# patterns_2 = ('/', '', '')
# for bar, pattern in zip(rects1, patterns_1):
#     bar.set_hatch(pattern)
# for bar, pattern in zip(rects2, patterns_2):
#     bar.set_hatch(pattern)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    i = 0
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height + error[rects][i]),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=16)
        i = i + 1


if __name__ == '__main__':
    # autolabel(rects1)
    # autolabel(rects2)

    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.ylim(0, 100)

    # ax.spines['right'].set_visible(False)
    # ax.spines['top'].set_visible(False)

    fig.set_size_inches(7.4, 4.4)
    fig.tight_layout()
    # plt.title("bookinfo")
    plt.savefig('bar-testone.eps', bbox_inches='tight')
    plt.show()
