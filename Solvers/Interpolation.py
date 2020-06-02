import numpy as np

if __name__ == "__main__":
    print("It's a computation file, please run \'main.py\'")


class Interpolator:
    y_diff = []
    x_values = []
    y_values = []
    y_graph_values = []
    dots_x = []
    dots_y = []
    equation_type = 0
    step = 0

    def __init__(self, x, y, types):
        self.x_values = x
        self.y_values = y
        self.start()
        self.step = self.x_values[1] - self.x_values[0]
        self.y_graph_values = []
        self.y_diff = []
        self.equation_type = types
        self.dots_x = []
        self.dots_y = []

    # def calculate(self, x):
    #     index = 0
    #     for l in self.x_values:
    #         if l > x:
    #             index = self.x_values.index(l)
    #     if index == len(self.x_values) - 2:
    #         index -= 1
    #     values = [self.x_values[0]]
    #     i = 0
    #     result = 0
    #     factor = 1
    #     while i < len(self.x_values):
    #         for k in range(0, i, 1):
    #             factor *= (x - self.x_values[i - 1])
    #         result += self.separated_differences(values) * factor
    #         # print(self.separated_differences(values))
    #         # print(factor)
    #         # print(i)
    #         i += 1
    #         if i != len(self.x_values):
    #             values.append(self.x_values[i])
    #     return result
    #
    # def start(self):
    #     for x in self.x_values:
    #         result = self.calculate(x)
    #         self.y_graph_values.append(result)

    def get_dots_value(self, x):
        y = self.interpolation(x)
        self.dots_x.append(x)
        self.dots_y.append(y)
        return y

    def get_function_value(self, x):
        if self.equation_type == 1:
            return np.power(x, 3) - 3 * np.power(x, 2) - abs(8 * x)
        elif self.equation_type == 2:
            return np.sin(x) + 2
        elif self.equation_type == 3:
            return 2 / x + x / 2
        elif self.equation_type == 4:
            return np.power(np.e, 2 * x) - 2

    def separated_differences(self, differences):
        if len(differences) == 1:
            return self.y_values[self.x_values.index(differences[0])]
        else:
            first = differences[0:len(differences) - 1]
            second = differences[1:len(differences)]
            return (self.separated_differences(second) - self.separated_differences(first)) / (
                    differences[-1] - differences[0])

    def interpolation(self, x):
        interpolation = self.y_diff[0][-1]
        n = len(self.x_values) - 2
        t = (x - self.x_values[-1]) / self.step
        i = 1
        while n >= 0:
            k = 1
            factor = t
            while k <= i - 1:
                factor *= (t + k) / (k+1)
                k += 1
            interpolation += factor * self.y_diff[i][n]
            n -= 1
            i += 1
        return interpolation

    def finite_differences(self):
        i = 1
        self.y_diff.append(self.y_values)
        while i < len(self.x_values):
            line = []
            j = 0
            while j < len(self.y_diff[i - 1]) - 1:
                result = self.y_diff[i - 1][j + 1] - self.y_diff[i - 1][j]
                line.append(result)
                j += 1
            self.y_diff.append(line)
            i += 1

