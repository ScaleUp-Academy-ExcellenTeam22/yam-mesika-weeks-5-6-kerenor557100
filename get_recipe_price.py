#submitted by Keren Or Hadad 208025205


def get_recipe_price(prices: dict,  *ingredients, optionals = []):
    """
    The function gets a dictionary of products and their prices per 100g, a list of ingredients and a
    list of optional ingredients. The function returns the total price of the mandatory ingredients (the ingredients
     that are not optional)
    :param prices: a dictionary where the key is the name of a product and the value is the price per 100g
    :param ingredients: The list of ingredients needed for the recipe.
    :param optionals: The list of optional ingredients ( which we won't buy).
    :return: Total price of the ingredients we bought for the recipe.
    """
    sum_price = 0
    for item in ingredients:
        item = item.split("=")
        if item[0] not in optionals:
            item[1] = int(item[1]) / 100
            sum_price += prices[item[0]] * item[1]
    return sum_price

print(get_recipe_price({'chocolate': 18, 'milk': 8}, "chocolate=300", optionals=['milk']))
"""
output:
54.0
"""