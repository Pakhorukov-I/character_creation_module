from math import sqrt


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверяет переданное значение и вычисляет квадратный корень."""
    if your_number <= 0:
        return

    root = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {root}')


message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')

print(message)
calc(25.5)
