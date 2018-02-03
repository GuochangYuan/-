def make_pizza(size,*toppings):
    """概述要制作的pizza"""
    print("\nMaking a "+str(size)+
            "-inch pizza with the folowing toppings:")
    for topping in toppings:
        print("-"+topping)