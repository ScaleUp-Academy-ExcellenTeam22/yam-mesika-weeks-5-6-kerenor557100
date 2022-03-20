#submitted by Keren Or Hadad 208025205


def add(args):
    result = zip(*args)
    lst_sum = []
    for it in result:
        coun = 0
        for i in it:
            coun += int(i)
        lst_sum.append(coun)
    return lst_sum


def zipwith(fun, *args):
    return fun(args)


print(zipwith(add, [1, 2, 3], [4, 5, 6]))
"""
output:
[5, 7, 9]
"""