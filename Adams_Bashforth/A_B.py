import matplotlib.pyplot as plt
from tabulate import tabulate
from art import *

print(logo)
print("*" * 200)


def func(x, y):
    """
    :return: returns function value by putting value of x and y.
    """
    res = (1 + y)
    return res


def predictor(y3, h, f3, f2, f1, f0):
    """
    :return: returns predictor value by putting values in formula -> y3 + (h / 24) * ((55 * f3) - (59 * f2) + (37 * f1)
    - (9 * f0))
    """
    y4p = round(y3 + (h / 24) * ((55 * f3) - (59 * f2) + (37 * f1) - (9 * f0)), 4)
    # y4p1 = round(y4p,4)
    print(f"Predictor Value , y4p = {y4p}\n")
    return y4p


def corrector(y3, h, f4p, f3, f2, f1):
    """
    :return: returns corrector value by putting values in formula -> y3 + (h / 24) * ((9 * f4p) + (19 * f3) - (5 * f2)
    + f1)
    """
    y4c = round(y3 + (h / 24) * ((9 * f4p) + (19 * f3) - (5 * f2) + f1), 4)
    # y4c1 = round(y4c,4)
    # print(f"Corrector Value, y4c = {y4c1}")
    return y4c


# Taking User inputs
x0 = float(input("Enter Value of x0: "))
x1 = float(input("Enter Value of x1: "))
x2 = float(input("Enter Value of x2: "))
x3 = float(input("Enter Value of x3: "))
x4 = float(input("Enter Value of x4: "))
y0 = float(input("Enter Value of y0: "))
y1 = float(input("Enter Value of y1: "))
y2 = float(input("Enter Value of y2: "))
y3 = float(input("Enter Value of y3: "))

# Tabulating the given data.
data = [[x0, y0],
        [x1, y1],
        [x2, y2],
        [x3, y3],
        [x4, "?"]]
print("\nGiven Values in tabulated form: ")
print(tabulate(data, headers=["x", "y"]))

print(f"\nWe have to find y({x4})\n")
h = round((x1 - x0), 4)
print(f"Value of h i.e.(x1-x0) is: {h}\n")

f0 = round(func(x0, y0), 4)
print(f"f0 = {f0}")
f1 = round(func(x1, y1), 4)
print(f"f1 = {f1}")
f2 = round(func(x2, y2), 4)
print(f"f2 = {f2}")
f3 = round(func(x3, y3), 4)
print(f"f3 = {f3}\n")

y4p = predictor(y3, h, f3, f2, f1, f0)
f4p = round(func(x4, y4p), 4)
print(f"f4p1 = {f4p}")
y4c = corrector(y3, h, f4p, f3, f2, f1)
print(f"Corrector Value, y4c1 = {y4c}\n")
count = 2
# While loop to check previous corector value is not equal to current value.
while y4c != y4p:
    y4p = y4c
    f4p = round(func(x4, y4p), 4)
    print(f"f4p{count} = {f4p}")
    y4c = corrector(y3, h, f4p, f3, f2, f1)
    print(f"Corrector Value, y4c{count} = {y4c}\n")

    count += 1

print(f"\nAs y4c{count - 1} = y4c{count - 2}.Therefore, y({x4}) = {y4c}\n\n\n")
print(end)

# Graph Plotting of the given function.
x_axis = [x0, x1, x2, x3, x4]
y_axis = [y0, y1, y2, y3, y4c]
plt.plot(x_axis, y_axis)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("x-y graph of given function")
plt.show()
