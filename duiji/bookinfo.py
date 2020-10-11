import numpy as np
import matplotlib.pyplot as plt

category_names = ['Strongly disagree', 'Disagree',
                  'Neither agree nor disagree', 'Agree', 'Strongly agree']
results = {
    'HTTP': [60, 20, 20, 0, 0],
    # 'gRPC': [26, 22, 29, 10, 13],
    'TCP': [50, 50, 0, 0, 0],
}
sum = [72,28]

def survey(results, category_names):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    # category_colors = plt.get_cmap('RdYlGn')(np.linspace(0.15, 0.85, data.shape[1]))
    category_colors = ['#3182bd', '#6baed6', '#9ecae1', '#c6dbef', '#eff3ff']
    category_colors_1 = ['#ef6548', '#fc8d59', '#fdbb84', '#fdd49e', '#fee8c8']

    fig, ax = plt.subplots()
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, 100)

    for i, (colname, color, new_color) in enumerate(zip(category_names, category_colors,category_colors_1)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        xcenters = starts + widths / 2
        colors = [color,new_color]
        ax.barh(labels, widths, left=starts, height=0.8,
                label=colname, color=color, edgecolor='black')

        # r, g, b  = color
        text_color = 'black'  # if r * g * b < 0.5 else 'darkgrey'
        flag = True

        for y, (x, c) in enumerate(zip(xcenters, widths)):
            if c != 0:
                ax.text(x, y, str(int(c)) + '%', ha='center', va='center', color=text_color, fontsize=14)
            # else:
            #     if flag:
            #         ax.text(x + 4, y, str(sum[y]) + '%', ha='center', va='center', color=text_color, fontsize=16)
            #         flag = False
    # ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
    #           loc='lower left', fontsize='small')

    return fig, ax


if __name__ == '__main__':
    fig, ax = survey(results, category_names)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    # plt.ylim(0, 38)

    # ax.spines['right'].set_visible(False)
    # ax.spines['top'].set_visible(False)

    fig.set_size_inches(11, 1.1)
    fig.tight_layout()
    plt.title('Bookinfo', fontsize = 16)

    plt.savefig('bookinfo-stack.eps', bbox_inches='tight')
    plt.show()
