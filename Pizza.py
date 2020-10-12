from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress',
                     'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping',
                    'mozzarella double_mozzarella '
                    'bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3  # in seconds for the sake of the example


class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f'preparing the {self.dough.name} '
              f'dough of your {self}...')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough')

    def validate_style(builders):
        try:
            input_msg = 'What pizza would you like, [m]argarita or [c]reamy bacon? '
            pizza_style = input(input_msg)
            builder = builders[pizza_style]()
            valid_input = True
        except KeyError:
            error_msg = 'Sorry, only margarita (key m) and creamy bacon (key c) are available'
            print(error_msg)
            return False, None
        return True, builder
