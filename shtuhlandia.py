#submitted by Keren Or Hadad 208025205

def shtuhlandia():
    special_states = []
    keyboard1 = {'q','w','e','r','t','y','u','i','o','p'}
    keyboard2 = {'a','s','d','f','g','h','j','k','l'}
    keyboard3 = {'z','x','c','v','b','n','m'}
    my_file = open("states.txt", "r")
    states = my_file.read()
    states_list = states.split("\n")
    my_file.close()
    for state in states_list:
        letters = set(list(state))
        if letters.issubset(keyboard1) or letters.issubset(keyboard2) or letters.issubset(keyboard3):
            special_states.append(state)
    print(special_states)


shtuhlandia()
"""
output:
['alaska']
"""