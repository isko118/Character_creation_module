from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """
    Вычисляет квадратный корень.

    Args:
        number (int or float):
        Число, из которого нужно извлечь квадратный корень.

    Returns:
        float: Квадратный корень из числа.

    """
    return sqrt(number)


def calc(your_number):
    """Печатает квадратный корень из числа."""
    if your_number <= 0:
        return 'Корень из отрицательного числа извлечь нельзя'

    result = calculate_square_root(your_number)
    name = (f'Мы вычислили квадратный корень из '
            f'введённого вами числа. Это будет: {result}')
    print(name)
    return None


calc(25.5)
print(message)
