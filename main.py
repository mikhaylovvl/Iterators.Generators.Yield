from FlatIterator import FlatIterator
from FlatGenerator import flat_generator


def main():
    nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None], ]
    # задание 1 вертикальный список, который обрабатывает списки с любым уровнем вложенности
    for item in FlatIterator(nested_list):
        print(item)
    # задание 1 плоский список, который обрабатывает списки с любым уровнем вложенности
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    # задание 2, который обрабатывает списки с любым уровнем вложенности
    nested_list = [['a', 'b', 'c'], ['d', 'e', 'f'], [1, 2, None], ]
    for item in flat_generator(nested_list):
        print(item)

    # задание 2 плоский список, который обрабатывает списки с любым уровнем вложенности
    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)


if __name__ == '__main__':
    main()
