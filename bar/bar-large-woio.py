import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

labels = ['200 services\n/ 180 policies ', '400 services\n/ 360 policies ', '600 services\n/ 540 policies ',
          '800 services\n/ 720 policies ', '1,000 services\n/ 900 policies ']
d_means = [2552, 5022, 7681, 10178, 12463]
d_woio_means = [2205, 4447, 6774, 8981, 11011]
# rd_means = [699, 1289, 1952, 2555, 3192]
# r_means = [1183, 2257, 3394, 4728, 6045]

d_std = [117, 104, 194, 238, 212]
d_woio_std = [93, 117, 140, 168, 163]
# r_std = [70, 30, 16, 169, 138]

e = [899, 1559, 2417, 3030, 3721]
bo = [d_means[0] - e[0], d_means[1] - e[1], d_means[2] - e[2], d_means[3] - e[3], d_means[4] - e[4]]

x = np.arange(len(labels))  # the label locations
width = 0.28  # the width of the bars
rwith = 0.28

# cmap = plt.get_cmap("tab20b")
# colors = cmap(np.array([, 9, 5]))
colors = ['#f7f7f7', '#0571b0', '#92c5de']

fig, ax = plt.subplots()
rects1 = ax.bar(x - 1 * width, d_means, rwith, yerr=d_std, error_kw=dict(capsize=6), label='Deployment',
                color=colors[0], align='edge', edgecolor='black')
rects2 = ax.bar(x , d_woio_means, rwith, yerr=d_woio_std, error_kw=dict(capsize=6), label='Deployment w/o IO',
                color=colors[2], align='edge',
                 edgecolor='black')
# rects3 = ax.bar(x + 0.5 * width, r_means, rwith, yerr=r_std, error_kw=dict(capsize=6), label='Removal', color=colors[2],
#                 align='edge', hatch="",
#                 edgecolor='black')

# rects4 = ax.bar(x -1.5*width, e, rwith, bottom=bo, label='Policy Generation', color='white', hatch="xxxx",align='edge', edgecolor='black')

error = {rects1: d_std, rects2: d_woio_std}
ax.set_ylabel('processing time (ms)', fontsize=13)

# Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('time (ms)', fontsize=14)
# ax.set_title('Scores by group and gender')
# red_patch = mpatches.Patch(facecolor='white', hatch='/', label='Policy Modification', edgecolor='black')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(handles=[rects1, rects2], fontsize=13)

# patterns_2 = ('/', '/', '/', '/', '/')
# for bar, pattern in zip(rects1, patterns_2):
#     bar.set_hatch(pattern)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    i = 0
    for rect in rects:
        xx = 3
        if rect.get_height() == 1724:
            xx = 8
        if rect.get_height() == 1406:
            xx = 2
        height = rect.get_height()
        ax.annotate('{:,}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 1.6, height + error[rects][i]),
                    xytext=(0, xx),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=12)
        i = i + 1


if __name__ == '__main__':
    autolabel(rects1)
    autolabel(rects2)
    # autolabel(rects3)

    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.ylim(0, 14000)
    # ax.grid(axis='y')

    # ax.spines['right'].set_visible(False)
    # ax.spines['top'].set_visible(False)

    fig.set_size_inches(9, 4.5)
    fig.tight_layout()
    plt.savefig('bar-large-woio.pdf', bbox_inches='tight')
    plt.show()
