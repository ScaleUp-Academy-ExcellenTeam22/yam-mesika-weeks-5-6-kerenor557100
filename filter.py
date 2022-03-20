#submitted by Keren Or Hadad 208025205


def filter(func, iter):
    return [x for x in iter if func(x)]


def is_even(num):
    mod = num % 2
    if mod == 0:
        return True
    return False


print (filter(is_even, [1,2,3,4,5,6,7]))
"""
output:
[2, 4, 6]
"""