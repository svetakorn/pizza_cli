import click
from pizza_classes import Margherita, Pepperoni, Hawaiian, bake, deliver, DEFAULT_SIZE, SIZE_CHOICES


PIZZAS = {
        'margherita': (Margherita, '🧀'),
        'pepperoni': (Pepperoni, '🌶'),
        'hawaiian': (Hawaiian, '🍍'),
    }


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True, help='Если указать, то заказ будет с доставкой')
@click.option('--size', default='L', help='Можно указать размер пиццы')
@click.argument('pizza', nargs=1)
def order(pizza: str, size: str, delivery: bool):
    """Позволяет сделать заказ и обрабатывает его"""
    if pizza not in PIZZAS.keys():
        print('Такой пиццы у нас нет :(')
        return
    if size not in SIZE_CHOICES:
        print('Такого размера пиццы у нас нет :(')
        return
    bake()
    if delivery:
        deliver()


@cli.command()
def menu():
    """Показывает меню без указания кол-ва ингредиентов"""
    print('А вот и наши пиццы! Пальчики оближешь :)\n'
          'Краткое описание ингредиентов:')

    for _, tup in PIZZAS.items():
        pizza_cls, emodji = tup
        pizza_dict = pizza_cls(DEFAULT_SIZE).dict()
        ingredients = list(pizza_dict.keys())
        print('- {0} {1}: {2}'.format(
            pizza_cls.name, emodji, ', '.join(ingredients)
        ))


@cli.command()
def full_menu():
    """Показывает подробное меню с количеством ингредиентов"""
    print('А вот и наши пиццы! Пальчики оближешь :)\n'
          'Полное описание ингредиентов:')

    for _, tup in PIZZAS.items():
        print('\n')
        pizza_cls, emodji = tup
        print(f'{pizza_cls.name} {emodji}')
        for k, v in pizza_cls(DEFAULT_SIZE).dict().items():
            print(f'{k} - {v} grams')


if __name__ == '__main__':
    cli()
