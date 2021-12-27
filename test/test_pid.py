# -*- encoding: UTF-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
import matplotlib.pyplot as plt
'''
@brief
'''


class TestingPID:
    def __init__(self):
        self.Kp = 0.5
        self.Ki = 0.5
        self.Kd = 2.5
        self.Resistance = -0.1
        self.loop = 300
        self.Ktop = {'p': 0.0, 'pi': 0.0, 'pid': 0.0}
        self.peak_time = {'p': 0, 'pi': 0, 'pid': 0}
        self.goal = 1.0
        self.dt = 0.1

    def test_p(self):
        output_sequence = []

        level = 0.2
        output_sequence.append(level)
        err = (self.goal - level) * self.dt
        u = self.Kp * err
        level += u + self.Resistance * self.dt
        output_sequence.append(level)
        for i in range(self.loop):
            err = (self.goal - level) * self.dt
            u = self.Kp * err
            level += u + self.Resistance * self.dt
            if level > self.Ktop['p']:
                self.Ktop['p'] = level
                self.peak_time['p'] = i + 2
            output_sequence.append(level)
        return output_sequence

    def test_pi(self):

        global Ktop
        output_sequence = []
        level = 0.2
        output_sequence.append(level)
        err = (self.goal - level) * self.dt
        his_err = 0
        his_err += err
        u = self.Kp * err + self.Ki * his_err
        level += u + self.Resistance * self.dt
        output_sequence.append(level)
        for i in range(self.loop):
            err = (self.goal - level) * self.dt
            his_err += err
            u = self.Kp * err + self.Ki * his_err
            level += u + self.Resistance * self.dt
            if level > self.Ktop['pi']:
                self.Ktop['pi'] = level
                self.peak_time['pi'] = i + 2
            output_sequence.append(level)
        return output_sequence

    def test_pid(self):
        output_sequence = []
        level = 0.2
        output_sequence.append(level)
        err = (self.goal - level) * self.dt
        e1 = err
        e2 = err
        his_err = 0
        his_err += err
        u = self.Kp * err +self. Ki * his_err + self.Kd * (e2 - e1)
        level += u + self.Resistance * self.dt
        output_sequence.append(level)
        for i in range(self.loop):
            err = (self.goal - level) * self.dt
            e2 = err
            his_err += err
            u = self.Kp * err + self.Ki * his_err + self.Kd * (e2 - e1)
            level += u + self.Resistance * self.dt
            if level > self.Ktop['pid']:
                self.Ktop['pid'] = level
                self.peak_time['pid'] = i + 2
            output_sequence.append(level)
            e1 = err
        return output_sequence

    def run(self):
        plt.figure(13)
        lim_y = 0.2
        range_y = 1.7
        ret1 = self.test_p()
        ret2 = self.test_pi()
        ret3 = self.test_pid()
        plt.subplot(1, 3, 1)
        plt.plot(ret1, 'k-')
        plt.plot([0, self.loop], [self.Ktop['p'], self.Ktop['p']], 'r-')
        plt.plot([0, self.loop], [self.goal, self.goal], 'g-')
        plt.xlim([0, self.loop])
        plt.ylim([lim_y, range_y * self.goal])
        plt.title('Proportion')

        plt.subplot(1, 3, 2)
        plt.plot(ret2, 'k-')
        plt.plot([0, self.loop], [self.Ktop['pi'], self.Ktop['pi']], 'r-')
        plt.plot([self.peak_time['pi'], self.peak_time['pi']], [0, self.Ktop['pi']], 'r-.')

        plt.plot([0, self.loop], [self.goal, self.goal], 'g-')
        plt.xlim([0, self.loop])
        plt.ylim([lim_y, range_y * self.goal])
        plt.title('Proportion Integral')

        plt.subplot(1, 3, 3)
        plt.plot(ret3, 'k-')
        plt.plot([0, self.loop], [self.Ktop['pid'], self. Ktop['pid']], 'r-')
        plt.plot([self.peak_time['pid'], self.peak_time['pid']], [0, self.Ktop['pid']], 'r-.')

        plt.plot([0, self.loop], [self.goal, self.goal], 'g-')
        plt.xlim([0, self.loop])
        plt.ylim([lim_y, range_y * self.goal])
        plt.title('Proportion Integral Derive')

        print('----------------'*10)
        print(self.Ktop)
        print(self.peak_time)
        plt.show()


pid_runner = TestingPID()
pid_runner.run()
