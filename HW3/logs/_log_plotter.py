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
    time3, x3, y3, theta3 = get_data('pos_task_6_k_3.csv')
    min_dim = np.minimum(time8.shape[0], time5.shape[0])-1

    plt.plot(time8[:min_dim], theta8[:min_dim], label=r"$K_{\Psi}=8$")
    plt.plot(time5[:min_dim], theta5[:min_dim], label=r"$K_{\Psi}=5$")
    plt.plot(time3[:min_dim], theta3[:min_dim], label=r"$K_{\Psi}=3$")
    plt.xlabel("Time [ms]")
    plt.ylabel(r"$\Theta$")
    plt.legend()
    plt.savefig('plots/task6.pdf')
    # plt.show()


def task8():
    time8, x8, y8, theta8 = get_data('pos_task_8_2.csv')
    goal = np.array([0, 0])
    error_x = x8-goal[0]
    error_y = y8-goal[1]
    error = np.sqrt((error_x)**2+(error_y)**2)
    start = np.array([0.7269, 0.5912])
    dist = start-goal
    plt.plot(time8, error)
    plt.xlim((0, np.max(time8)))
    plt.ylim((0, np.max(error)+0.05))
    plt.xlabel("Time [ms]")
    plt.ylabel("Distance to start point [m]")
    # plt.savefig('plots/task8.pdf')
    plt.show()

def task9():
    time, x, y, theta = get_data('pos_task_9.csv')
    goal = np.array([0.7269, 2.0382])
    start = np.array([0,0])
    theta_goal = np.arctan2(goal[1],goal[0])*180/np.pi
    error = theta_goal - theta
    d0 = np.cos(theta)*(start[0])
    # error_y = y-goal[1]
    # error = np.sqrt((error_x)**2+(error_y)**2)
    # dist = start-goal
    plt.plot(time, error)
    # plt.xlim((0, np.max(time)))
    # plt.ylim((0, np.max(error)+0.05))
    plt.xlabel("Time [ms]")
    plt.ylabel(r"Error in $\theta$")
    # plt.savefig('plots/task8.pdf')
    plt.show()

def task11():
    time8, x8, y8, theta8 = get_data('pos_task_11_k_8.csv')
    time5, x5, y5, theta5 = get_data('pos_task_11_k_5.csv')
    time3, x3, y3, theta3 = get_data('pos_task_11_k_3.csv')
    min_dim = np.minimum(time8.shape[0], time5.shape[0])-1

    plt.subplot(1,2,1)
    plt.plot(time8[:min_dim], x8[:min_dim], label=r"$K_{\Psi}=8$")
    plt.plot(time5[:min_dim], x5[:min_dim], label=r"$K_{\Psi}=5$")
    plt.plot(time3[:min_dim], x3[:min_dim], label=r"$K_{\Psi}=3$")
    plt.xlabel("Time [ms]")
    plt.ylabel(r"$x$")
    plt.legend()

    plt.subplot(1,2,2)
    plt.plot(time8[:min_dim], y8[:min_dim], label=r"$K_{\Psi}=8$")
    plt.plot(time5[:min_dim], y5[:min_dim], label=r"$K_{\Psi}=5$")
    plt.plot(time3[:min_dim], y3[:min_dim], label=r"$K_{\Psi}=3$")
    plt.xlabel("Time [ms]")
    plt.ylabel(r"$y$")
    plt.legend()
    plt.savefig('plots/task11.pdf')

def task14():
    time10, x10, y10, theta10 = get_data('pos_task_14_k_5.csv')
    p = 0.4 # meters
    x_g = 0.7269
    y_g = 2.0382
    theta10 = np.deg2rad(theta10)
    theta_g = np.arctan2(2.0382,0.7269)
    d_p = np.sin(theta_g)*(x10+p*np.cos(theta10)-0) - np.cos(theta_g)*(y10+p*np.sin(theta10)-0)

    plt.plot(time10, d_p, label=r"$d_{p}$")
    plt.xlabel("Time [ms]")
    plt.legend()
    plt.tight_layout()

    plt.savefig('plots/task14.pdf')
    plt.show()

def task15():
    p = 0.4 # meters
    time10, x10, y10, theta10 = get_data('pos_task_15.csv')
    x_g = 0.7269
    y_g = 2.0382
    theta10 = np.deg2rad(theta10)
    theta_g = np.arctan2(2.0382,0.7269)
    d_g = np.cos(theta_g)*(x_g-x10)+np.sin(theta_g)*(y_g-y10)
    d_p = np.sin(theta_g)*(x10+p*np.cos(theta10)-0) - np.cos(theta_g)*(y10+p*np.sin(theta10)-0)

    plt.subplot(1,2,1)

    plt.plot(time10, d_g, label=r"$d_{g}$")
    plt.xlabel("Time [ms]")
    plt.legend()

    plt.subplot(1,2,2)

    plt.plot(time10, d_p, label=r"$d_{p}$")
    plt.xlabel("Time [ms]")
    plt.legend()
    plt.tight_layout()

    plt.savefig('plots/task15.pdf')
    plt.show()


if __name__ == "__main__":
    # task6()
    # task8()
    task9()
