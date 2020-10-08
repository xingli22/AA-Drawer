import matplotlib.pyplot as plt
import numpy as np

recipe = ["225 g flour",
          "90 g sugar",
          "1 egg",
          "225 g flour",
          "90 g sugar",
          "1 egg",
          "60 g butter",
          "100 ml milk",
          "1/2 package of yeast"]

labels = ["Bookinfo", "Hipster Shop", "Sock Shop"]

if __name__ == '__main__':
    fig, ax = plt.subplots()

    size = 0.36
    vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

    cmap = plt.get_cmap("tab20b")
    aaa=[1,9,13]
    bbb=['#EEA140','#153760','#8D1A10']
    ccc=['#F7C553','#FBE2A3','#2E5D95','#91B7DF','#D26D6A','#EFBFBD']
    outer_colors = cmap(np.array(aaa))
    inner_colors = cmap(np.array([aaa[0]+1, aaa[0]+2, aaa[1]+1, aaa[1]+2,aaa[2]+1,aaa[2]+2]))

    wedges_o, texts_o = ax.pie(vals.sum(axis=1), radius=1 - size, colors=bbb,
                               wedgeprops=dict(width=size, edgecolor='w'))  # , labels=labels,
    # textprops=dict(fontsize=12))

    wedges_i, texts_i = ax.pie(vals.flatten(), radius=1, colors=ccc,
                               wedgeprops=dict(width=size, edgecolor='w', zorder=2))

    # ax.set(aspect="equal", title='Pie plot with `ax.pie`')

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=1, va="center")

    # for i, p in enumerate(wedges_o):
    #     ang = (p.theta2 - p.theta1) / 2. + p.theta1
    #     y = np.sin(np.deg2rad(ang))
    #     x = np.cos(np.deg2rad(ang))
    #     horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    #     connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    #     kw["arrowprops"].update({"connectionstyle": connectionstyle})
    #     ax.annotate(recipe[i], xy=(x, y), xytext=(1.2 * np.sign(x), 1.4 * y),
    #                 horizontalalignment=horizontalalignment, **kw, fontsize=12)

    ax.legend(wedges_o, labels,
              title="Ingredients",
              title_fontsize=12,
              loc="best",
              fontsize=12,
              bbox_to_anchor=(1, 0, 0.5, 1))

    # plt.setp(autotexts_o, size=12, weight="bold")

    for i, p in enumerate(wedges_i):
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        # ax.annotate(recipe[i], xy=(x * size, y * size), xytext=(1.35 * np.sign(x), 1.4 * y),
        ax.annotate(recipe[i], xy=(x, y), xytext=(1.2 * np.sign(x), 1.2 * y),
                    horizontalalignment=horizontalalignment, **kw, fontsize=12)

    fig = plt.gcf()

    plt.tight_layout()
    # fig.set_size_inches(8, 4)
    plt.savefig('pie.eps', bbox_inches='tight')
    plt.show()
