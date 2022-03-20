#submitted by Keren Or Hadad 208025205


def mepo_lepo(func, iter):
    result = []
    for item in iter:
        result.append(func(item))
    return result


def add2(num):
    return num+2


print(mepo_lepo(add2,iter([1,2,3])))
"""
output:
[3, 4, 5]
"""
