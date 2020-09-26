from matplotlib import pyplot as plt
import numpy as np
from math import sin, cos, pi


def ctrv(x, y, v, yaw, yaw_rate, dt, t):
    predicted_states_list = []
    start_state = np.array([x, y, v, yaw, yaw_rate])
    predicted_states_list.append(start_state)
    last_state = start_state
    for i in range(int(t/dt)):
        state_change_rate = np.array([(last_state[2]/last_state[4])*(sin(last_state[3] + last_state[4] * dt) - sin(last_state[3])),
                                      (last_state[2] / last_state[4]) * (- cos(last_state[3] + last_state[4] * dt) + cos(last_state[3])),
                                      0,
                                      yaw_rate * dt,
                                      0
                                      ])
        next_state = last_state + state_change_rate
        predicted_states_list.append(next_state)
        last_state = next_state

    return predicted_states_list

if __name__ == "__main__":
    predicted_states = ctrv(x=1, y=1, v=5, yaw=0, yaw_rate=pi/2, dt=0.02, t=4)
    x = np.array(predicted_states)[:, 0]
    y = np.array(predicted_states)[:, 1]
    plt.plot(x, y)
    # plt.axis([0,5,0,5])
    plt.show()


