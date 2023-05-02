# Стек

from typing import Optional, Union


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item: str) -> None:
        self.items.append(int(item))

    def pop(self) -> None:
        if not len(self.items):
            raise IndexError('error')
        self.items.pop()

    def get_max(self) -> int:
        if not len(self.items):
            raise IndexError('None')
        return max(self.items)


def input_data() -> list:
    n = int(input())
    data = [input() for _ in range(n)]
    return data


def make_magik(stack: StackMax, el: str) -> Optional[Union[int, str]]:
    command, *value = el.split()
    call = getattr(stack, command)
    try:
        return call(*value)
    except IndexError as e:
        return e.args[0]


def algorithm(data: list) -> list:
    stack = StackMax()
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
    res = algorithm(['get_max', 'push 7', 'pop', 'push -2', 'push -1', 'pop',
                     'get_max', 'get_max'])
    assert res == ['None', -2, -2]


if __name__ == '__main__':
    main()
