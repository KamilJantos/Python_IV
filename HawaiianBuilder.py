from MargaritaBuilder import MargaritaBuilder
from Pizza import *


class HawaiianBuilder(MargaritaBuilder):

    def __init__(self):
        self.pizza = Pizza('hawaiian')
        self.progress = PizzaProgress.queued
        self.baking_time = 8  # in seconds for the sake of the example

    def prepare_dough(self):
        super().prepare_dough()

    def add_sauce(self):
        print('adding the tomato sauce to your hawaiian...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        topping_desc = 'double mozzarella, oregano, pineapple, chicken'
        topping_items = (PizzaTopping.double_mozzarella,
                         PizzaTopping.oregano)
        print(f'adding the topping ({topping_desc}) to your hawaiian')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping ({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your hawaiian for {self.baking_time} seconds')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your hawaiian is ready')
