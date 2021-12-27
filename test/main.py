# -*- encoding: UTF-8 -*-
import matplotlib.pyplot as plt
# mass-spring-damper system


class PID:
    def __init__(self):
        self.loop = 100
        self.__mass = 1.0  # kg
        self.b = 10  # N s/m
        self.k = 20  # N/m
        self.F = 1  # N
        self.goal = 0.9

    def P(self, Kp):
        output_sequence = []

        for i in range(self.loop):
            output_sequence.append(1.0 - 1.0 / (i * i + 10.0 * i + 20.0))
        return output_sequence

    def run(self):
        # F = kx + bx' + mx''
        # x 位移， x' 速度， x''加速度
        # 拉普拉斯变换F(s) = kX(s) + bsX(s) + ms^2X(s)
        # X(s) / F(s) = 1 / (ms^2 + bs + k)
        # X(s) / F(s) = 1 / (s^2 + 10s + 20)
        ret = self.P(1)
        print(ret)
        plt.figure(13)
        lim_y = 0.0
        range_y = 1.7
        plt.subplot(1, 3, 1)
        plt.plot(ret, 'k-')
        # plt.plot([0, self.loop], [self.Ktop['p'], self.Ktop['p']], 'r-')
        # plt.plot([0, self.loop], [self.goal, self.goal], 'g-')
        plt.xlim([0, self.loop])
        plt.ylim([lim_y, range_y * self.goal])
        plt.title('Proportion')
        plt.show()


_pid_test = PID()
_pid_test.run()
