#submitted by Keren Or Hadad 208025205

from os import listdir as dirs

# part 5.1
def zo_haderech(path: str):
    """

    :param path: A path to the folder where the images can be found.
    :return: Returns all the pictures which their names starts with the word "deep"
    """

    return [name for name in dirs(path) if name.startswith("deep")]



print(zo_haderech(r"images"))
"""
output:
['deeper.svg', 'deeper2.svg']
"""