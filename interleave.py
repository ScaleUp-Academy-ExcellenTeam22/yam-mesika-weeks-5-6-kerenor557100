#submitted by Keren Or Hadad 208025205
# part 5.4
import itertools


def interleave(*lists):
    if len(set(len(_) for _ in lists)) > 1:
        raise ValueError("Lists are not all the same length!")
    joint = list(itertools.chain(*lists))
    for l_idx, li in enumerate(lists):
        joint[l_idx::len(lists)] = li
    return joint

print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
"""
output:
['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
"""