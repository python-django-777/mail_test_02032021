def set_test_1(x):
    # тест на структуру данных set
    assert type(x) == set, 'set_test_1: x не является структурой данных set'


def set_test_2(x):
    # тест на структуру данных set, квадратный корень из суммы значений x это целое число
    assert type(x) == set, 'set_test_1: x не является структурой данных set'
    assert sum(x) ** 0.5 % 1 == 0, 'Квадратный корень из суммы значений x не является целым числом'


def set_test_3(x):
    # тест на структуру данных set
    assert type(x) == set, 'set_test_1: x не является структурой данных set'
    try:
        assert sum(x) ** 0.5 % 1 == 0, 'Квадратный корень из суммы значений x не является целым числом'
    except AssertionError:
        pass


def int_test_1(x):
    # тест на структуру данных int
    assert type(x) == int, 'int_test_1: x не является структурой данных int'


def int_test_2(x):
    # тест на структуру данных int, тест квадратный корень из x это целое число
    assert type(x) == int, 'int_test_2: x не является структурой данных int'
    assert x ** 0.5 % 1 == 0, 'Квадратный корень из x не является целым числом'


def int_test_3(x):
    # тест на структуру данных int
    assert type(x) == int, 'int_test_2: x не является структурой данных int'
    try:
        assert x ** 0.5 % 1 == 0, 'Квадратный корень из x не является целым числом'
    except AssertionError:
        pass
