# Стек. Максимальный эл. за О(1)

from typing import Optional, Union


class StackMaxEffective:
    def __init__(self):
        self.__items: list = []
        self.__max_items: list = [float('-inf')]

    def push(self, item: str) -> None:
        item = int(item)
        self.__items.append(item)
        if item >= self.__max_items[-1]:
            self.__max_items.append(item)

    def pop(self) -> None:
        if self.__is_empty():
            raise IndexError('error')
        item = self.__items.pop()
        if item == self.__max_items[-1]:
            self.__max_items.pop()

    def get_max(self) -> int:
        if self.__is_empty():
            raise IndexError('None')
        return self.__max_items[-1]

    def __is_empty(self) -> bool:
        return not self.__items


def input_data() -> list:
    n = int(input())
    return [input() for _ in range(n)]


def make_magik(stack: StackMaxEffective, el: str) -> Optional[Union[int, str]]:
    command, *value = el.split()
    call = getattr(stack, command)
    try:
        return call(*value)
    except IndexError as e:
        return e.args[0]


def algorithm(data: list) -> list:
    stack = StackMaxEffective()
    result = []
    for el in data:
        res = make_magik(stack, el)
        if res is not None:
            result.append(res)
    return result


def main() -> None:
    data = input_data()
    res = algorithm(data)
    print(*res, sep='\n')


def test():
    res = algorithm(['pop', 'pop', 'push 4', 'push -5', 'push 7', 'pop', 'pop',
                     'get_max', 'pop', 'get_max'])
    assert res == ['error', 'error', 4, 'None']


if __name__ == '__main__':
    main()
