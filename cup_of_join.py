#submitted by Keren Or Hadad 208025205

#part 5.2

def cup_of_join(*args, sep = '-'):
    lst_return = []
    for arg in args:
        for item in arg:
            lst_return.append(item)
        if args[-1] != arg:
            lst_return.append(sep)
    return lst_return
print(cup_of_join([2, 4, 3],[6],[7, 2], sep='@'))

"""
output:
[2, 4, 3, '@', 6, '@', 7, 2]
"""
