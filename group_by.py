#submitted by Keren Or Hadad 208025205

def group_by(func, iter):
    dict = {}
    for item in iter:
        key = func(item)
        if key not in dict.keys():
            dict[key] = []
        dict[key].append(item)
    return dict


words = ["hi", "bye", "yo", "try"]
print(group_by(len, words))

""" 
output:
{2: ['hi', 'yo'], 3: ['bye', 'try']}

"""
