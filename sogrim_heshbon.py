#submitted by Keren Or Hadad 208025205


#part 6.2
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


functions = {"+": add, "-": subtract, "*": multiply, "/": divide}


def sogrim_heshbon(num1, num2, op):
    return functions[op](num1, num2)


print(sogrim_heshbon(3, 6, "+"))
print(sogrim_heshbon(2, 8, "*"))


"""
output:
9
16
"""
