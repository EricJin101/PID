#-*- encoding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import matplotlib.pyplot as plt

class TestingPID:
    def __init__(self):
        self.Kp = 0.5
        self.Ki = 0.4
        self.Kd = 0.3
        self.Resistance = -0.1
        self.loop = 30
        self.Ktop = 0
        self.goal = 1.0

    def test_p(self):
        output_sequence = []

        level = 0.2
        output_sequence.append(level)
        err = self.goal - level
        u = self.Kp * err
        level += u + self.Resistance
        output_sequence.append(level)
        for i in range(self.loop):
            err = self.goal - level
            u = self.Kp * err
            level += u + self.Resistance
            output_sequence.append(level)
        return output_sequence

    def test_pi(self):

        global Ktop
        output_sequence = []
        # u = Kp * e
        # goal = 1.0
        level = 0.2
        output_sequence.append(level)
        err = self.goal - level
        his_err = 0
        his_err += err
        u = self.Kp * err + self.Ki * his_err
        level += u + self.Resistance
        output_sequence.append(level)
        for i in range(self.loop):
            err = self.goal - level
            his_err += err
            u = self.Kp * err + self.Ki * his_err
            level += u + self.Resistance
            if level > self.Ktop:
                Ktop = level
            output_sequence.append(level)
        return output_sequence

    def test_pid(self):
        output_sequence = []
        # u = Kp * e
        # goal = 1.0
        level = 0.2
        output_sequence.append(level)
        err = self.goal - level
        e1 = err
        e2 = err
        his_err = 0
        his_err += err
        u = self.Kp * err +self. Ki * his_err + self.Kd * (e2 - e1)
        level += u + self.Resistance
        output_sequence.append(level)
        for i in range(self.loop):
            err = self.goal - level
            e2 = err
            his_err += err
            u = self.Kp * err + self.Ki * his_err + self.Kd * (e2 - e1)
            level += u + self.Resistance
            output_sequence.append(level)
            e1 = err
        return output_sequence

    def run(self):
        plt.figure(13)

        ret1 = self.test_p()
        ret2 = self.test_pi()
        ret3 = self.test_pid()
        plt.subplot(1,3,1)
        plt.plot(ret1, 'g-')
        plt.plot([0,30],[self.Ktop, self.Ktop], 'r-')
        plt.plot([0,30],[self.goal, self.goal], 'b-')
        plt.xlim([0, self.loop])
        plt.ylim([0, 2])

        plt.subplot(1,3,2)
        plt.plot(ret2, 'g-')
        plt.plot([0,30],[self.Ktop, self.Ktop], 'r-')
        plt.plot([0,30],[self.goal, self.goal], 'b-')
        plt.xlim([0, self.loop])
        plt.ylim([0, 2])

        plt.subplot(1,3,3)
        plt.plot(ret3, 'g-')
        plt.plot([0,30],[self.Ktop,self. Ktop], 'r-')
        plt.plot([0,30],[self.goal, self.goal], 'b-')
        plt.xlim([0, self.loop])
        plt.ylim([0, 2])
        # i = 0
        # while i < len(ret2):
        #     print(ret3[i] - ret2[i])
        #     i += 1

        plt.show()


pid_runner = TestingPID()
pid_runner.run()
