# %%
import numpy as np

EXECTIME = 6/1000
T = np.array([20, 29, 35])/1000
TOTTIME = 4060


class Pend():
    def __init__(self, prio, exectime):
        self.prio = prio
        self.release_time = 0
        self.computation = 0
        self.has_finished = False
