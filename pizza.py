def making_pizzas(size, *toppings):
    """Выводит описание пиццы"""
    print('\nMaking a ' + str(size)+
        '-inch pizza with following toppings:')
    for topping in toppings:
        print('- ' + topping)

