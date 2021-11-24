"""
Coffee Machine task, steps 1 - 3
"""


def coffee_machine_steps():
    # first step
    coffee_create_steps = '''Starting to make a coffee 
Grinding coffee beans 
Boiling water 
Mixing boiled water with crushed coffee beans 
Pouring coffee into the cup 
Pouring some milk into the cup 
Coffee is ready! '''

    print(coffee_create_steps)


def coffee_machine_prepare():
    # second step
    water_for_one_cup = 200
    milk_for_one_cup = 50
    beans_for_one_cup = 15

    count_of_cups = input('Write how many cups of coffee you will need: ')

    ingredient_quantity_water = int(count_of_cups) * water_for_one_cup
    ingredient_quantity_milk = int(count_of_cups) * milk_for_one_cup
    ingredient_quantity_beans = int(count_of_cups) * beans_for_one_cup

    ingredient_quantity = f'''For {count_of_cups} cups of coffee you will need: 
{ingredient_quantity_water} ml of water 
{ingredient_quantity_milk} ml of milk 
{ingredient_quantity_beans} g of coffee beans 
'''

    print(ingredient_quantity)


def coffee_ingredients_bin():
    # step 3
    count_of_water = int(input('Write how many ml of water the coffee machine has: '))
    count_of_milk = int(input('Write how many ml of milk the coffee machine has: '))
    count_of_beans = int(input('Write how many grams of beans the coffee machine has: '))
    count_of_cups = int(input('Write how many cups of coffee you will need: '))

    min_water = 200
    min_milk = 50
    min_beans = 15

    real_count_of_cups = min(count_of_water // min_water, count_of_milk // min_milk, count_of_beans // min_beans)

    if real_count_of_cups == count_of_cups:
        print('Yes, I can make that amount of coffee')
    elif real_count_of_cups > count_of_cups:
        print(f'Yes, I can make that amount of coffee (and even {real_count_of_cups - count_of_cups} more than that)')
    else:
        print(f'No, I can make only {real_count_of_cups} cups of coffee')


if __name__ == '__main__':
    coffee_ingredients_bin()
