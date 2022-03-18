#submitted by Keren Or Hadad 208025205


def get_recipe_price(d_ing: dict,  *args, optionals = []):
    sum_price = 0
    for item in args:
        item = item.split("=")
        if item[0] not in optionals:
            item[1] = int(item[1]) / 100
            sum_price += d_ing[item[0]] * item[1]
    return sum_price

print(get_recipe_price({'chocolate': 18, 'milk': 8}, "chocolate=300", optionals=['milk']))
"""
output:
54.0
"""