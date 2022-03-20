#submitted by Keren Or Hadad 208025205

def be_hello(input):
    input = input.split(" ")
    item = []
    for x in input:
        item.append(len(x))
    return item


print(be_hello("Toto, I've a feeling we're not in Kansas anymore"))
print(be_hello("i love you!"))

"""
output:
[5, 4, 1, 7, 5, 3, 2, 6, 7]
[1, 4, 4]
"""