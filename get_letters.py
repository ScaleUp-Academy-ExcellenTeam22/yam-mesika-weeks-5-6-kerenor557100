#submitted by Keren Or Hadad 208025205


def get_letters(): #o_ohel_p_python
    lst_tv = [chr(tv_capital) for tv_capital in range(ord('A'), ord('Z')+1)]
    lst_tv.extend([chr(tv) for tv in range(ord('a'), ord('z')+1)])
    return lst_tv


print(get_letters())

"""
output:
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

"""
