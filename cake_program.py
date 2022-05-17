ingredient_list_c = {'Flour': '15.8%', 'Sugar': '24.5%', 'Unsweetened Cocoa Powder': '5.6%',
                     'Butter milk': '18.0%', 'Boiling Water': '17.0%', 'Others': '19.1'}
ingredient_list_r = {'Flour': '22.4%', 'Sugar': '22.4%', 'Canola': '24%',
                     'Butter milk': '17.9%', 'other': '13.3'}
ingredient_list_l = {'Flour': '15.6%', 'Sugar': '15.0%', 'Filling': '30.7%', 'others': '38.7%'}


def print_recipe(cake_list):
    """
    For the cake with different type and different size, the ingredient is different.
    The cake type was passed to this function from the main function.
    Now we print the recipe depends on the cake size.
    """
    cake_size = input("Please select cake size, 'R' for regular, 'L' for large: ")

    if cake_size.upper() == 'R':
        print(f"The ingredient list is below: ")
        for ingredient, ratio in cake_list.items():
            # the ingredient weight of regular cake, unit was changed from lb to oz
            r_weight = float(ratio.strip('%')) * 64 / 100
            print("%-28s%5.1f oz" % (ingredient, r_weight))

    elif cake_size.upper() == 'L':
        print(f"The ingredient list is below: ")
        for ingredient, ratio in cake_list.items():
            # the ingredient weight of large cake, unit was changed from lb to oz
            l_weight = float(ratio.strip('%')) * 112 / 100
            print("%-28s%5.1f oz" % (ingredient, l_weight))

    else:
        print("Please select the cake size again: ")
        return print_recipe(cake_list)


def cake_recipe():
    """
    The purpose of this function is to select cake type, and pass the selection to another function
    :return:
    """
    cake_type = input("Please select cake type, "
                      "'1' for Chocolate, '2' for Red velvet, '3' for lemon, or 'q' to quit: ")
    while True:
        if cake_type == '1':
            return print_recipe(ingredient_list_c)
        elif cake_type == '2':
            return print_recipe(ingredient_list_r)
        elif cake_type == '3':
            return print_recipe(ingredient_list_l)
        elif cake_type == 'q':
            print("I prefer to eat in restaurant.")
            break
        else:
            print("Please select again.")
            return cake_recipe()


if __name__ == '__main__':
    cake_recipe()
