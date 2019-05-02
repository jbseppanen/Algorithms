#!/usr/bin/python

import math


# First Pass
def recipe_batch(recipe, ingredients):
    max_batches = None
    for r in recipe:
        if r not in ingredients:
            return 0
        batches = (ingredients[r] // recipe[r])
        if max_batches is None:
            max_batches = batches
        elif batches < max_batches:
            max_batches = batches
    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batch(recipe, ingredients), ingredients=ingredients))

# print(recipe_batch({'milk': 100, 'butter': 50, 'flour': 5}, {'milk': 132, 'butter': 48, 'flour': 51}))
