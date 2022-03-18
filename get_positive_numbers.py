#submitted by Keren Or Hadad 208025205


def get_positive_numbers(input):
    item = []
    for x in input:
        if x >= 0:
            item.append(int(x))
    return item


print(get_positive_numbers([2, 4, 5, -5, -6, 9]))
print(get_positive_numbers([2, 4.3, 5, -5.2, -6, 9]))

"""
output:
[2, 4, 5, 9]
[2, 4, 5, 9]
"""