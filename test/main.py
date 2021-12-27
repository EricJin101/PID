#-*- encoding: UTF-8 -*-
from pprint import pprint
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
E = - 0.1
Kp = 0.5
Ki = 0.4
Kd = 0.3
NUM = 30
Ktop = 0
goal = 1.0

def test_p():
    output_sequence = []
    # u = Kp * e
    # goal = 1.0
    level = 0.2
    output_sequence.append(level)
    err = goal - level
    u = Kp * err
    level += u + E
    output_sequence.append(level)
    for i in range(NUM):
        err = goal - level
        u = Kp * err
        level += u + E
        output_sequence.append(level)
    return output_sequence
    # plt.plot(output_sequence, 'g-')
    # pprint(output_sequence)
    # plt.show()

def test_pi():

    global Ktop
    output_sequence = []
    # u = Kp * e
    # goal = 1.0
    level = 0.2
    output_sequence.append(level)
    err = goal - level
    his_err = 0
    his_err += err
    u = Kp * err + Ki * his_err
    level += u + E
    output_sequence.append(level)
    for i in range(NUM):
        err = goal - level
        his_err += err
        u = Kp * err + Ki * his_err
        level += u + E
        if level > Ktop:
            Ktop = level
        output_sequence.append(level)
    return output_sequence
    # plt.subplot(1,2,1)
    # plt.plot(output_sequence, 'g-')
    # pprint(output_sequence)
    # plt.show()

def test_pid():
    output_sequence = []
    # u = Kp * e
    # goal = 1.0
    level = 0.2
    output_sequence.append(level)
    err = goal - level
    e1 = err
    e2 = err
    his_err = 0
    his_err += err
    u = Kp * err + Ki * his_err + Kd * (e2 - e1)
    level += u + E
    output_sequence.append(level)
    for i in range(NUM):
        err = goal - level
        e2 = err
        his_err += err
        u = Kp * err + Ki * his_err + Kd * (e2 - e1)
        print(Kd * (e2 - e1))
        level += u + E
        output_sequence.append(level)
        e1 = err
    return output_sequence
    # plt.subplot(1,2,2)
    # plt.plot(output_sequence, 'g-')
    # pprint(output_sequence)
    # plt.show()

def main(arg):
    x_raw = [1]
    y_raw = [1]
    t_yaw = [1]
    plt.figure(13)

    ret1 = test_p()
    ret2 = test_pi()
    ret3 = test_pid()
    plt.subplot(1,3,1)
    plt.plot(ret1, 'g-')
    plt.plot([0,30],[Ktop, Ktop], 'r-')
    plt.plot([0,30],[goal, goal], 'b-')
    plt.xlim([0, NUM])
    plt.ylim([0, 2])

    plt.subplot(1,3,2)
    plt.plot(ret2, 'g-')
    plt.plot([0,30],[Ktop, Ktop], 'r-')
    plt.plot([0,30],[goal, goal], 'b-')
    plt.xlim([0, NUM])
    plt.ylim([0, 2])

    plt.subplot(1,3,3)
    plt.plot(ret3, 'g-')
    plt.plot([0,30],[Ktop, Ktop], 'r-')
    plt.plot([0,30],[goal, goal], 'b-')
    plt.xlim([0, NUM])
    plt.ylim([0, 2])
    # i = 0
    # while i < len(ret2):
    #     print(ret3[i] - ret2[i])
    #     i += 1

    plt.show()


if __name__ == "__main__":
    main(str(sys.argv[1]))