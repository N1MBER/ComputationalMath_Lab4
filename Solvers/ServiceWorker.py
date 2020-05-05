import numpy as np
import matplotlib.pyplot as plt
from Solvers import Interpolation
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

if __name__ == "__main__":
    print("It's a computation file, please run \'main.py\'")


class ServiceWorker:
    type_equation = 0
    x_values = []
    y_values = []
    mode = 0
    with_y = 0
    count_of_dots = 0

    def __init__(self, mode):
        self.mode = mode
        self.select_equation()
        self.set_abscissa()
        self.set_ordinate()
        interpolator = Interpolation.Interpolator(self.x_values, self.y_values, self.type_equation)
        interpolator.start()
        make_graph(interpolator)
        check_dots(interpolator)
        del interpolator

    def select_equation(self):
        while 1:
            try:
                print("Please choose equation:\n"
                      "\t1. f(x) = x^3 - 2x^2 + 8x\n"
                      "\t2. f(x) = sin(x) + 2\n"
                      "\t3. f(x) = 2/x + x/2\n"
                      "\t4. f(x) = e^2x - 2\n")
                answer = int(input('Equation: ').strip())
                if 0 < answer < 5:
                    self.type_equation = answer
                    break
                else:
                    getReadyAnswer(1)
                    continue
            except ValueError:
                getReadyAnswer(1)
                continue
            except TypeError:
                getReadyAnswer(1)
                continue

    def set_abscissa(self):
        while 1:
            if self.mode == 1:
                try:
                    self.x_values = []
                    print("Please set dot's:")
                    dots = list(input("Dots: ").strip().split(" "))
                    if len(dots) < 2:
                        getReadyAnswer(1)
                        continue
                    else:
                        self.count_of_dots = len(dots)
                        for i in dots:
                            self.x_values.append(float(i.strip()))
                        break
                except ValueError:
                    getReadyAnswer(1)
                    continue
                except TypeError:
                    getReadyAnswer(1)
                    continue
            elif self.mode == 2:
                try:
                    self.x_values = []
                    count = int(input("How many dot's? : ").strip())
                    if count < 2:
                        getReadyAnswer(1)
                        continue
                    else:
                        step = float(input("Which step? : ").strip())
                        if step <= 0:
                            getReadyAnswer(1)
                            continue
                        else:
                            start = float(input("Which start point? :").strip())
                            self.count_of_dots = count
                            self.x_values.append(start)
                            i = 1
                            while i < count:
                                self.x_values.append(self.x_values[i - 1] + step)
                                i += 1
                            break
                except ValueError:
                    getReadyAnswer(1)
                    continue
                except TypeError:
                    getReadyAnswer(1)
                    continue
            else:
                return

    def set_ordinate(self):
        while 1:
            try:
                print("How do you want to set \'y\':\n"
                      "\t1. By yourself\n"
                      "\t2. Default from function\n")
                answer = int(input("Variant: ").strip())
                if answer == 1:
                    self.with_y = 1
                elif answer == 2:
                    self.with_y = 0
                else:
                    getReadyAnswer(1)
                    continue
            except ValueError:
                getReadyAnswer(1)
                continue
            except TypeError:
                getReadyAnswer(1)
                continue
            self.y_values = []
            if self.with_y:
                ordinates = list(input("Ordinates: ").strip().split(" "))
                if len(ordinates) != self.count_of_dots:
                    getReadyAnswer(1)
                    continue
                else:
                    for i in ordinates:
                        try:
                            self.y_values.append(get_function_value(self.type_equation, float(i.strip())))
                        except ZeroDivisionError:
                            getReadyAnswer(1)
                            continue
                        except TypeError:
                            getReadyAnswer(1)
                            continue
                        except ValueError:
                            getReadyAnswer(1)
                            continue
                    break
            else:
                for i in self.x_values:
                    try:
                        self.y_values.append(get_function_value(self.type_equation, i))
                    except ZeroDivisionError:
                        self.y_values.append(get_function_value(self.type_equation, i + 1e-9))
                break


def get_function_value(equation, x):
    if equation == 1:
        return np.power(x, 3) - 2 * np.power(x, 2) + 8 * x
    elif equation == 2:
        return np.sin(x) + 2
    elif equation == 3:
        return 2 / x + x / 2
    elif equation == 4:
        return np.power(np.e, 2 * x) - 2
    else:
        getReadyAnswer(1)
        return


def check_dots(calculator):
    while 1:
        try:
            print("Do you want to know the value at a point?\n"
                  "\t1. Yes\n"
                  "\t2. No\n")
            answer = int(input("Answer: ").strip())
            if answer == 1:
                dot = float(input("Dot: ").strip())
                calculator.get_dots_value(dot)
                make_graph(calculator)
            elif answer == 2:
                break
            else:
                getReadyAnswer(1)
                continue
        except TypeError:
            getReadyAnswer(1)
            continue
        except ValueError:
            getReadyAnswer(1)
            continue


def getReadyAnswer(type_answer):
    if type_answer == 1:
        print("Incorrect input.\n")
    elif type_answer == 2:
        print("No solution.\n")
    elif type_answer == 3:
        print("There is no concrete solution or it doesn't exist.\n")
    elif type_answer == 4:
        print("Convergence condition is not satisfied on this segment.\n")
    elif type_answer == 5:
        print("Counts of iteration reached 2.5 million , solution not found.\n")
    elif type_answer == 6:
        print("The initial approximation is poorly selected, solution not found.\n")
    elif type_answer == 7:
        print("Counts of iteration reached 250 thousand , solution not found.\n")


def make_graph(calculator):
    try:
        ax = plt.gca()
        plt.grid()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        equations = {1: "f(x) = x^3 - 2x^2 + 8x",
                     2: "f(x) = sin(x) + 2",
                     3: "f(x) = 2/x + x/2",
                     4: "f(x) = e^2x - 2"}
        plt.title("Graphic of " + equations[calculator.equation_type])
        if len(calculator.dots_x) == 0:
            x = np.linspace(min(calculator.x_values), max(calculator.x_values), 100)
        else:
            minimum = min(calculator.x_values)
            maximum = max(calculator.x_values)
            for i in calculator.dots_x:
                if i < minimum:
                    minimum = i
                elif i > maximum:
                    maximum = i
            x = np.linspace(minimum, maximum, 100)
        first_equation = [calculator.calculate(i) for i in x]
        second_equation = [get_function_value(calculator.equation_type, k) for k in x]
        plt.plot(x, first_equation, color='b', linewidth=2)
        plt.plot(x, second_equation, color='r', linewidth=2)
        j = 0
        for i in calculator.x_values:
            plt.scatter(i, calculator.y_graph_values[j], color='b', s=40)
            j += 1
        k = 0
        if len(calculator.dots_x) != 0:
            for i in calculator.dots_x:
                plt.scatter(i, calculator.dots_y[k], color='g', s=40)
                k += 1
        plt.show()
        del x
    except ValueError:
        return
    except ZeroDivisionError:
        return
