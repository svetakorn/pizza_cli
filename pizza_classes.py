import time
import random
from decorators import log


DEFAULT_SIZE = 'L'
SIZE_CHOICES = ('XL', 'L')


class BasePizza:
    tomato_sauce: int = 50
    mozzarella: int = 150
    size: str = DEFAULT_SIZE

    def __init__(self, size: str = None):
        if size in SIZE_CHOICES:
            self.size = size
        else:
            print('У нас только размеры {0} - а по умолчанию готовим {1}'.format(
                ', '.join(SIZE_CHOICES), DEFAULT_SIZE
            ))

    def dict(self):
        return {'tomato_sauce': self.tomato_sauce,
                'mozzarella': self.mozzarella}

    def __eq__(self, other_pizza):
        return self.size == other_pizza.size and self.dict() == self.dict()


class Margherita(BasePizza):
    name = 'Margherita'
    tomatoes: int = 200

    def dict(self):
        ing_dict = super().dict()
        ing_dict.update({'tomatoes': self.tomatoes})
        return ing_dict


class Pepperoni(BasePizza):
    name = 'Pepperoni'
    pepperoni: int = 180

    def dict(self):
        ing_dict = super().dict()
        ing_dict.update({'pepperoni': self.pepperoni})
        return ing_dict


class Hawaiian(BasePizza):
    name = 'Hawaiian'
    chicken: int = 210
    pineapples: int = 120

    def dict(self):
        ing_dict = super().dict()
        ing_dict.update({'chicken': self.chicken,
                         'pineapples': self.pineapples})
        return ing_dict


@log('🍕 Приготовили за {} сек!')
def bake():
    time.sleep(random.randint(1, 2))


@log('🛵 Доставили за {} сек!')
def deliver():
    time.sleep(random.randint(1, 3))
