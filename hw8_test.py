class Food(object):
    def drink(self):
        return ['Water', 'Cola']

    def allergen(self):
        return []


class Meat(Food):
    def drink(self):
        return ['Red wine'] + super().drink()


class Milk(Food):
    def allergen(self):
        return ['Milk-protein'] + super().allergen()


class Flour(Food): pass


class Rabbit(Meat):
    def drink(self):
        return ['Novello wine'] + super().drink()


class Pork(Meat):
    def drink(self):
        return ['Sovinion wine'] + super().drink()

    def allergen(self):
        return ['Pork-protein'] + super().allergen()


class Pasty(Milk, Flour): pass


class Pie(Rabbit, Pork, Pasty):
    def drink(self):
        return ['Mineral water'] + super().drink()


if __name__ == "__main__":
    pie = Pie()


    print('List of allergens: ')
    for allergen in pie.allergen(): print(' - ' + allergen)

    print('List of recommended drinks: ')
    for drink in pie.drink(): print(' - ' + drink)
