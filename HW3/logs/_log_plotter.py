import numpy as np
from matplotlib import pyplot as plt
import csv
import sys
np.set_printoptions(threshold=sys.maxsize)
plt.style.use('ggplot')


def get_data(filename):
    with open(filename) as csv_file:
        raw = np.array(list(csv.reader(csv_file, delimiter=';'))
                       )[1:].astype("float64")
        time = raw[:, 0]-raw[0, 0]
        x = raw[:, 1]
        y = raw[:, 2]
        theta = raw[:, 3]
    return time, x, y, theta


def task6():
    time8, x8, y8, theta8 = get_data('pos_task_6_k_8.csv')
    time5, x5, y5, theta5 = get_data('pos_task_6_k_5.csv')
    min_dim = np.minimum(time8.shape[0], time5.shape[0])-1

    plt.plot(time8[:min_dim], theta8[:min_dim], label=r"$K_{\Psi}=8$")
    plt.plot(time5[:min_dim], theta5[:min_dim], label=r"$K_{\Psi}=5$")
    plt.xlabel("Time [ms]")
    plt.ylabel(r"$\Theta$")
    plt.legend()
    plt.savefig('plots/task6.pdf')
    # plt.show()


def task8():
    time8, x8, y8, theta8 = get_data('pos_task_8.csv')
    goal = np.array([0.7269, 0.5912])
    error_x = x8-goal[0]
    error_y = y8-goal[1]
    error = np.sqrt((error_x)**2+(error_y)**2)
    start = np.array([0, 0])
    dist = start-goal
    plt.plot(time8, error)
    plt.xlim((0, np.max(time8)))
    plt.ylim((0, np.max(error)+0.05))
    plt.xlabel("Time [ms]")
    plt.ylabel("Distance from start point [m]")
    plt.savefig('plots/task8.pdf')
    # plt.show()


if __name__ == "__main__":
    task8()
