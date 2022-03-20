#submitted by Keren Or Hadad 208025205
# part 6.3
import math


def tipul_shoresh(midot):
    result = []
    for item in midot:
        try:
            if int(item) or item == '0':
                result.append(math.sqrt(eval(item)))
        except ValueError:
            try:
                if float(item):
                    result.append(math.sqrt(eval(item)))
            except ValueError:
                pass
    return result


print(tipul_shoresh(['100', '25.0', '12a', 'mEoW', '0']))
"""
output:
[10.0, 5.0, 0.0]
"""
