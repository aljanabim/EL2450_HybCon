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
    # time8, x8, y8, theta8 = get_data('pos_task_8_2.csv')
    # goal = np.array([0, 0])
    # error_x = x8-goal[0]
    # error_y = y8-goal[1]
    # error = np.sqrt((error_x)**2+(error_y)**2)
    # start = np.array([0.7269, 0.5912])
    # dist = start-goal
    # plt.plot(time8, error)
    # plt.xlim((0, np.max(time8)))
    # plt.ylim((0, np.max(error)+0.05))
    # plt.xlabel("Time [ms]")
    # plt.ylabel("Distance to start point [m]")

    lim = 600
    time8, x8, y8, theta8 = get_data('pos_task_8.csv')
    time8, x8,y8,theta8 = time8[:lim], x8[:lim], y8[:lim], theta8[:lim]

    time, x, y, theta = get_data('pos_task_9.csv')
    time, x,y,theta = time[:lim], x[:lim], y[:lim], theta[:lim]
    goal = np.array([0.7269, 2.0382])
    start = np.array([0,0])

    distance8 = np.sqrt(np.power(y8,2)+np.power(x8,2))
    distance = np.sqrt(np.power(y,2)+np.power(x,2))

    plt.plot(time8,distance8, label=r"distance to true start with $\omega=0$ ")
    plt.plot(time,distance, label=r"distance to true start")
    plt.xlabel("Time [ms]")
    plt.legend()
    # plt.ylabel(r"$d_0$")
    # plt.suptitle("Both parts of the controller activated")
    plt.tight_layout()
    plt.savefig('plots/task8.pdf')

    plt.show()




def task9():
    lim = 600
    time, x, y, theta = get_data('pos_task_9.csv')
    time, x,y,theta = time[:lim], x[:lim], y[:lim], theta[:lim]
    goal = np.array([0.7269, 2.0382])
    # start = np.array([0.7269,0.5912])
    start = np.array([0,0])

    theta_goal = np.arctan2(goal[1],goal[0])*180/np.pi
    error = theta_goal - theta
    d0 = np.cos(np.deg2rad(theta))*(start[0]-x)+np.sin(np.deg2rad(theta))*(start[1]-y)
    distance = np.sqrt(np.power(y,2)+np.power(x,2))
    # print(np.power(y,2))
    plt.subplot(1,2,1)
    plt.plot(time, error)
    # plt.xlim((0, np.max(time)))
    # plt.ylim((0, np.max(error)+0.05))
    plt.xlabel("Time [ms]")
    plt.ylabel(r"Error in $\theta$")
    plt.subplot(1,2,2)
    plt.plot(time,d0, label=r"$d_0$")
    plt.xlabel("Time [ms]")
    plt.legend()
    # plt.ylabel(r"$d_0$")
    # plt.suptitle("Both parts of the controller activated")
    plt.tight_layout()
    plt.savefig('plots/task9.pdf')

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

def task18():
    time, x, y, theta = get_data('pos_task_18.csv')
    plt.plot(x,y,'k',label='Actual path')
    w_x = [-1.25,
           -0.75,
           -0.25,
           -0.25,
            0.25,
            0.25,
           ]
    w_y = [1.25,
           1.25,
           1.25,
           0.75,
           0.75,
           0.25,
           ]
    plt.plot(w_x,w_y,'bv',label='Waypoints')
    plt.xlim([-1.5,1.5])
    plt.ylim([-1.5,1.5])
    plt.xlabel("X [m]")
    plt.ylabel("Y [m]")
    plt.legend()
    plt.savefig('plots/task18.pdf')
    plt.show()

def task13():
    time, x1, y1, theta = get_data('pos_task_13_p1.csv')
    time, x2, y2, theta = get_data('pos_task_13_p40.csv')
    time, x3, y3, theta = get_data('pos_task_13_p80.csv')
    plt.plot(y1,x1,'r',label='$p=1$')
    plt.plot(y2,x2,'g',label='$p=40$')
    plt.plot(y3,x3,'b',label='$p=80$')
    plt.legend()
    plt.ylim([-0.25,1.0])
    plt.axis('equal')
    plt.xlabel('Y [m]')
    plt.ylabel('X [m]')
    plt.tight_layout()
    plt.savefig('plots/task13.pdf')
    plt.show()

if __name__ == "__main__":
    # task6()
    task8()
    task9()
    task13()
