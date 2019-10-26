def make_pizza(size, *toppings):
    print("Making a " + str(size) +
          '-inch pizza with the following toppings:')
    for topping in toppings:
        print("- " + topping)

make_pizza(32,'Mushrooms','Pepporoni','Olives','Ham','Onions','Peppers','Anchovies','Ground Beef')
