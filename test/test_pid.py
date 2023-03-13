# -*- encoding: UTF-8 -*-
import matplotlib.pyplot as plt
'''
假设水箱，需要将水位维持在1m处
水箱每秒漏0.1m
每次添加
P： Kp * (1m - 当前水位)
PI： Kp * (1m - 当前水位) + Ki × （每次加水误差和）
PID： Kp * (1m - 当前水位) + Ki × （每次加水误差和）+ Kd * (本次误差 - 上次误差)
'''

# 这样的系统本身就是积分，因为水位是累加的
# 如果是电机，那么输入降低，“水位”不维持，会降低


class TestingPID:
    def __init__(self):
        self.Kp = 0.5
        self.Ki = 0.5
        self.Kd = 2.9
        self.Resistance = -0.1
        self.loop = 300
        self.Ktop = {'p': 0.0, 'pi': 0.0, 'pid': 0.0}
        self.peak_time = {'p': 0, 'pi': 0, 'pid': 0}
        self.goal = 1.0
        self.dt = 0.1

    def test_p(self):
        # 存在稳态误差
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
        # 可能超调

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

        print('----------------'*5)
        print(self.Ktop)
        print(self.peak_time)
        plt.show()


pid_runner = TestingPID()
pid_runner.run()
