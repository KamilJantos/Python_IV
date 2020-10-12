class Pizza:
    def __init__(self, builder):
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese
        self.mozarella = builder.mozarella
        self.ham = builder.ham
        self.mushrooms = builder.mushrooms
        self.redOnions = builder.redOnions
        self.oregano = builder.oregano
        self.bacon = builder.bacon
        self.chicken = builder.chicken
        self.pineapple = builder.pineapple

    def __str__(self):
        garlic = 'yes' if self.garlic else 'no'
        cheese = 'yes \n' if self.extra_cheese else 'no \n'
        mozarella = 'yes\n' if self.mozarella else 'no\n'
        ham = 'yes\n' if self.ham else 'no\n'
        mushrooms = 'yes\n' if self.mushrooms else 'no\n'
        redOnions = 'yes\n' if self.redOnions else 'no\n'
        oregano = 'yes\n' if self.oregano else 'no\n'
        bacon = 'yes\n' if self.bacon else 'no\n'
        chicken = 'yes\n' if self.chicken else 'no\n'
        pineapple = 'yes\n' if self.pineapple else 'no\n'

        info = (f'Garlic: {garlic}',
                f'Extra cheese: {cheese}'
                f'Mozarella: {mozarella}'
                f'Ham: {ham}'
                f'Mushrooms: {mushrooms}'
                f'Red Onions: {redOnions}'
                f'Oregano: {oregano}'
                f'Bacon: {bacon}'
                f'Chicken: {chicken}'
                f'Pineapple: {pineapple}'
                )
        return '\n'.join(info)

    class PizzaBuilder:
        def __init__(self, name):
            self.name = name
            self.extra_cheese = False
            self.garlic = False
            self.mozarella = False
            self.ham = False
            self.mushrooms = False
            self.redOnions = False
            self.oregano = False
            self.bacon = False
            self.chicken = False
            self.pineapple = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def add_mozarella(self):
            self.mozarella = True
            return self

        def add_ham(self):
            self.ham = True
            return self

        def add_mushrooms(self):
            self.mushrooms = True
            return self

        def add_redOnions(self):
            self.redOnions = True
            return self

        def add_oregano(self):
            self.oregano = True
            return self

        def add_bacon(self):
            self.bacon = True
            return self

        def add_chicken(self):
            self.chicken = True
            return self

        def add_pineapple(self):
            self.pineapple = True
            return self

        def build(self):
            return Pizza(self)


def build_margarita():
    return Pizza.PizzaBuilder('Margarita').add_extra_cheese().add_garlic().build()


def build_creamy_bacon():
    return Pizza.PizzaBuilder('Creamy bacon').add_bacon() \
        .add_ham() \
        .add_mushrooms() \
        .add_redOnions() \
        .add_oregano() \
        .build()


def build_hawaiian():
    return Pizza.PizzaBuilder('Hawaiian').add_bacon()\
        .add_ham()\
        .add_mozarella()\
        .add_redOnions()\
        .add_oregano()\
        .add_pineapple()\
        .add_chicken()\
        .build()


def validate_style(builders):
    try:
        input_msg = 'What pizza would you like, [m]argarita, [c]reamy bacon or [h]awaiian? '
        pizza_style = input(input_msg)
        builder = builders[pizza_style]
        valid_input = True
    except KeyError:
        error_msg = 'Sorry, only margarita (key m), creamy bacon (key c) and hawaiian (key h) are available'
        print(error_msg)
        return False, None
    return True, builder


def main():
    pizzaType = dict(m=build_margarita(), c=build_creamy_bacon(), h=build_hawaiian())
    valid_input = False
    while not valid_input:
        valid_input, pizza = validate_style(pizzaType)
    print()
    print(f'Enjoy your pizza!')
    print(f'Yours pizza contains: \n')
    print(f'{pizza}')


if __name__ == '__main__':
    main()
