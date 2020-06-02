import numpy as np
import matplotlib.pyplot as plt
from Solvers import Interpolation
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

if __name__ == "__main__":
    print("It's a computation file, please run \'main.py\'")


class ServiceWorker:
    mode = 0
    type_equation = 0
    x_values = []
    y_values = []
    with_y = 0
    count_of_dots = 0

    ready_data = {1: [[-2, -1, 0, 1],[-2,-1.7,-1.4,-1.1,-0.8,-0.5,-0.2,0.1,0.4,0.7,1],[0,10,20,30,40,50,60,70,80,90]],
                  2: [[0, np.pi/2,np.pi,3*np.pi/2,2*np.pi],[0,np.pi/6,np.pi/3,np.pi/2,2*np.pi/3,5*np.pi/6,np.pi,7*np.pi/6,4*np.pi/3,3*np.pi/2,5*np.pi/3,11*np.pi/6,2*np.pi],
                      [0,5*np.pi,10*np.pi,15*np.pi,20*np.pi,25*np.pi,30*np.pi,35*np.pi,40*np.pi,45*np.pi,50*np.pi]],
                  3: [[0,1,2,3],[0,0.5,1,1.5,2,2.5,3],[0,5,10,15,20,25,30,35,40,45,50]],
                  4: [[0,1,2,3],[0,0.5,1,1.5,2,2.5,3],[0,5,10,15,20,25,30,35,40,45,50]]
    }
    ready_txt = {1: ["[-2, -1, 0, 1]","[-2,-1.7,-1.4,-1.1,-0.8,-0.5,-0.2,0.1,0.4,0.7,1]","[0,10,20,30,40,50,60,70,80,90]"],
                  2: ["[0, np.pi/2,np.pi,3*np.pi/2,2*np.pi]","[0,np.pi/6,np.pi/3,np.pi/2,2*np.pi/3,5*np.pi/6,np.pi,7*np.pi/6,4*np.pi/3,3*np.pi/2,5*np.pi/3,11*np.pi/6,2*np.pi]",
                      "[0,5*np.pi,10*np.pi,15*np.pi,20*np.pi,25*np.pi,30*np.pi,35*np.pi,40*np.pi,45*np.pi,50*np.pi]"],
                  3: ["[0,1,2,3]","[0,0.5,1,1.5,2,2.5,3]","[0,5,10,15,20,25,30,35,40,45,50]"],
                  4: ["[0,1,2,3]","[0,0.5,1,1.5,2,2.5,3]","[0,5,10,15,20,25,30,35,40,45,50]"]
    }

    def __init__(self, mode):
        self.mode = mode
        self.x_values = []
        self.y_values = []
        self.select_equation()
        self.start()
        interpolator = Interpolation.Interpolator(self.x_values, self.y_values, self.type_equation)
        interpolator.finite_differences()
        make_graph(interpolator)
        check_dots(interpolator)
        del interpolator

    def start(self):
        if self.mode == 2:
            self.set_abscissa()
            self.set_ordinate()
        elif self.mode == 1:
            while 1:
                print("Please choose a type\n"
                      "\t1. small interval and 4-5 dots: " + self.ready_txt[self.type_equation][0] + "\n"
                      "\t2. small interval and 10-11 dots" + self.ready_txt[self.type_equation][1] + "\n"
                      "\t3. change value of function for one x\n"
                      "\t4. big interval and 10-11 dots" + self.ready_txt[self.type_equation][2] + "\n")
                answer = int(input("Variant: ").strip())
                if answer == 1:
                    self.x_values = self.ready_data[self.type_equation][0]
                    for i in self.x_values:
                        try:
                            self.y_values.append(get_function_value(self.type_equation, i))
                        except ZeroDivisionError:
                            self.y_values.append(get_function_value(self.type_equation, i + 1e-9))
                    break
                elif answer == 2:
                    self.x_values = self.ready_data[self.type_equation][1]
                    for i in self.x_values:
                        try:
                            self.y_values.append(get_function_value(self.type_equation, i))
                        except ZeroDivisionError:
                            self.y_values.append(get_function_value(self.type_equation, i + 1e-9))
                    break
                elif answer == 3:
                    self.x_values = self.ready_data[self.type_equation][1]
                    for i in self.x_values:
                        try:
                            self.y_values.append(get_function_value(self.type_equation, i))
                        except ZeroDivisionError:
                            self.y_values.append(get_function_value(self.type_equation, i + 1e-9))
                    print("Write number of dots which you want to change\n")
                    number = int(input("Number: ").strip())
                    if 1 <= number <= len(self.ready_data[self.type_equation][2]):
                        value = float(input("Value for this dot: ").strip())
                        self.y_values[number - 1] = value
                    else:
                        getReadyAnswer(1)
                        continue
                    break
                elif answer == 4:
                    self.x_values = self.ready_data[self.type_equation][2]
                    for i in self.x_values:
                        try:
                            self.y_values.append(get_function_value(self.type_equation, i))
                        except ZeroDivisionError:
                            self.y_values.append(get_function_value(self.type_equation, i + 1e-9))
                else:
                    getReadyAnswer(1)
                    continue


    def select_equation(self):
        while 1:
            try:
                print("Please choose equation:\n"
                      "\t1. f(x) = x^3 - 3x^2 - 8|x|\n"
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
            try:
                self.x_values = []
                print("Please set interval [a;b]\n")
                count = list(input("[a ;b]: ").strip().split())
                if len(count) == 2:
                    a = float(count[0].strip())
                    b = float(count[1].strip())
                    if b < a:
                        getReadyAnswer(1)
                        continue
                    print("How many dots?\n")
                    dots = int(input("Dots: ").strip())
                    if dots < 2:
                        getReadyAnswer(1)
                        continue
                    step = (b - a) / dots
                    i = a
                    while i <= b:
                        self.x_values.append(i)
                        i += step
                    self.count_of_dots = dots
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

    def set_ordinate(self):
        while 1:
            try:
                print("How do you want to set \'y\':\n"
                      "\t1. From function\n"
                      "\t2. All from function and one by yourself\n")
                answer = int(input("Variant: ").strip())
                if answer == 1:
                    for i in self.x_values:
                        try:
                            self.y_values.append(get_function_value(self.type_equation, i))
                        except ZeroDivisionError:
                            self.y_values.append(get_function_value(self.type_equation, i + 1e-9))
                    break
                elif answer == 2:
                    for i in self.x_values:
                        try:
                            self.y_values.append(get_function_value(self.type_equation, i))
                        except ZeroDivisionError:
                            self.y_values.append(get_function_value(self.type_equation, i + 1e-9))
                    print("Write number of dots which you want to change\n")
                    number = int(input("Number: ").strip())
                    if 1 <= number <= self.count_of_dots:
                        value = float(input("Value for this dot: ").strip())
                        self.y_values[number - 1] = value
                    else:
                        getReadyAnswer(1)
                        continue
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


def get_function_value(equation, x):
    if equation == 1:
        return np.power(x, 3) - 3 * np.power(x, 2) - abs(8 * x)
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
                result = calculator.get_dots_value(dot)
                print(result)
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
        equations = {1: "f(x) = x^3 - 3x^2 - 8|x|",
                     2: "f(x) = sin(x) + 2",
                     3: "f(x) = 2/x + x/2",
                     4: "f(x) = e^2x - 2"}
        plt.title("Graphic of " + equations[calculator.equation_type])
        minimum = min(calculator.x_values)
        maximum = max(calculator.x_values)
        if len(calculator.dots_x) != 0:
            for i in calculator.dots_x:
                if i < minimum:
                    minimum = i
                elif i > maximum:
                    maximum = i
        x = np.linspace(minimum, maximum, 100)
        first_equation = [calculator.interpolation(i) for i in x]
        second_equation = [get_function_value(calculator.equation_type, k) for k in x]
        plt.plot(x, first_equation, color='b', linewidth=2)
        plt.plot(x, second_equation, color='r', linewidth=2)
        j = 0
        for i in calculator.x_values:
            plt.scatter(i, calculator.y_values[j], color='b', s=40)
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
