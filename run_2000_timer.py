#submitted by Keren Or Hadad 208025205
import time


def add_loop(num):
    res = 0
    for i in range(1000):
        time.sleep(0.01)
        res += int(num[0])
    return res


def run_2000_timer(f, *items):
    start_time = time.time()
    f(items)
    return time.time() - start_time


print(run_2000_timer(print, "Hello"), ' seconds')
print(run_2000_timer(add_loop, 2), ' seconds')
""" 
output:
0.0  seconds
15.873172998428345  seconds
"""
