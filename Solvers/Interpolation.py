import numpy as np

if __name__ == "__main__":
    print("It's a computation file, please run \'main.py\'")


class Interpolator:
    x_values = []
    y_values = []
    y_graph_values = []
    dots_x = []
    dots_y = []
    equation_type = 0

    def __init__(self, x, y, types):
        self.x_values = x
        self.y_values = y
        self.y_graph_values = []
        self.equation_type = types
        self.dots_x = []
        self.dots_y = []

    def calculate(self, x):
        values = [self.x_values[0]]
        i = 0
        result = 0
        while i < len(self.x_values):
            factor = 1
            for k in range(0, i, 1):
                factor *= (x - self.x_values[i - 1])
            result += self.separated_differences(values) * factor
            i += 1
            if i != len(self.x_values):
                values.append(self.x_values[i])
        return result

    def start(self):
        for x in self.x_values:
            result = self.calculate(x)
            self.y_graph_values.append(result)

    def get_dots_value(self, x):
        y = self.calculate(x)
        self.dots_x.append(x)
        self.dots_y.append(y)

    def get_function_value(self, x):
        if self.equation_type == 1:
            return np.power(x, 3) - 2 * np.power(x, 2) + 8 * x
        elif self.equation_type == 2:
            return np.sin(x) + 2
        elif self.equation_type == 3:
            return 2 / x + x / 2
        elif self.equation_type == 4:
            return np.power(np.e, 2 * x) - 2

    def separated_differences(self, differences):
        try:
            if len(differences) == 1:
                return self.get_function_value(differences[0])
            else:
                first = differences[0:len(differences) - 1]
                second = differences[1:len(differences)]
                return (self.separated_differences(second) - self.separated_differences(first)) / (
                        differences[-1] - differences[0])
        except ZeroDivisionError:
            return (self.get_function_value(differences[1] + 1e-9) - self.get_function_value(differences[0] + 1e-9)) / (
                    differences[1] - differences[0])
