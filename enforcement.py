import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 50, 10)
x = (1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
y = (0.16, 0.17, 0.19, 0.22, 0.23, 0.24, 0.29, 0.31, 0.3, 0.34, 0.35)

if __name__ == '__main__':
    plt.figure()
    plt.ylabel('time (ms)', fontsize=16)
    plt.xlabel('# of policies', fontsize=16)

    a = ['%.2f' % oi for oi in np.linspace(0, 0.5, 20)]  # Y轴的刻度标签，为字符串形式，.2f表示小数点两位
    b = [eval(oo) for oo in a]  # Y轴的刻度
    plt.yticks(b, a)

    #plt.aspect = 1

    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    plt.plot(x, y, 'o-')
    fig = plt.gcf()

    plt.tight_layout()
    fig.set_size_inches(8, 4)
    plt.savefig('enforcement.eps')
    plt.show()
