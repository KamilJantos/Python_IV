from CreamyBaconBuilder import *
from HawaiianBuilder import *


def validate_style(builders):
    try:
        input_msg = 'What pizza would you like, [m]argarita,  [c]reamy bacon or [h]awaiian? '
        pizza_style = input(input_msg)
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError:
        error_msg = 'Sorry, only margarita (key m) and creamy bacon (key c) are available'
        print(error_msg)
        return False, None
    return True, builder


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        steps = (builder.prepare_dough,
                 builder.add_sauce,
                 builder.add_topping,
                 builder.bake)
        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder, h=HawaiianBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f'Enjoy your {pizza}!')


if __name__ == '__main__':
    main()
