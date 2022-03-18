#submitted by Keren Or Hadad 208025205

from os import listdir as dirs

# part 5.1
def zo_haderech(path: str):
    item = []
    for filename in dirs(path):
        if filename[:4] == "deep":
            item.append(filename)
    return item



print(zo_haderech(r"images"))
"""
output:
['deeper.svg', 'deeper2.svg']
"""