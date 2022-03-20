#submitted by Keren Or Hadad 208025205
import functools
#part 5.2

def cup_of_join(*args, sep = '-'):
    """
    gets list of lists, join them while separating them with the character in parameter "sep".
    :param args: list of lists to join
    :param sep: separator
    :return: joint list with separator between the lists.
    """
    lst_return = functools.reduce(lambda a, b:a+[sep]+b, args)
    return lst_return


print(cup_of_join([2, 4, 3],[6],[7, 2], sep='@'))

"""
output:
[2, 4, 3, '@', 6, '@', 7, 2]
"""
