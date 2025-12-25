recipe = {
    "flour": 500,
    "sugar": 200,
    "eggs": 3,
    "milk": 100,
    "vanilla": 5
}

pantry = {
    "flour": 400,
    "eggs": 10,
    "milk": 100,
}

shopping_list = {}

for ingredient, amount_needed in recipe.items():
    
    if ingredient in pantry:
        amount_have = pantry[ingredient]
    else:
        amount_have = 0

    difference = amount_needed - amount_have

    if difference > 0:
        shopping_list[ingredient] = difference

print("Shopping List:")
for ingredient, amount_needed in shopping_list.items():
    print(f"{ingredient}: {amount_needed}")
