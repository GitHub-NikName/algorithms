# Дек на кольцевом буфере. О(1)

from typing import Tuple, List, Optional


class Deque:
    def __init__(self, n: int):
        self.__deque: list = [None] * n
        self.__max_size: int = n
        self.__head: int = 0
        self.__tail: int = -1
        self.__size: int = 0

    def push_back(self, value: str) -> None:
        self.__is_full()
        self.__push(self.__tail, value)
        self.__tail = self.__get_index(self.__tail, -1)

    def push_front(self, value: str) -> None:
        self.__is_full()
        self.__push(self.__head, value)
        self.__head = self.__get_index(self.__head, 1)

    def pop_back(self) -> str:
        self.__is_empty()
        self.__tail = self.__get_index(self.__tail, 1)
        return self.__pop(self.__tail)

    def pop_front(self) -> str:
        self.__is_empty()
        self.__head = self.__get_index(self.__head, -1)
        return self.__pop(self.__head)

    def __push(self, index: int, value: str) -> None:
        self.__deque[index] = value
        self.__size += 1

    def __pop(self, index: int) -> str:
        x = self.__deque[index]
        self.__deque[index] = None
        self.__size -= 1
        return x

    def __get_index(self, index: int, inc: int) -> int:
        return (index + inc) % self.__max_size

    def __is_empty(self) -> None:
        if self.__size == 0:
            raise IndexError

    def __is_full(self) -> None:
        if self.__size == self.__max_size:
            raise IndexError


def input_data() -> Tuple[int, List[str]]:
    n, m = int(input()), int(input())
    commands = [input() for _ in range(n)]
    return m, commands


def deque_proc(deq: Deque, el: str) -> Optional[str]:
    cmd, *val = el.split()
    call = getattr(deq, cmd)
    try:
        return call(*val)
    except IndexError:
        return 'error'


def algorithm(m: int, data: list) -> list:
    deq = Deque(m)
    result = []
    for el in data:
        res = deque_proc(deq, el)
        if res:
            result.append(res)
    return result


def main() -> None:
    m, data = input_data()
    res = algorithm(m, data)
    print(*res, sep='\n')


def test():
    res = algorithm(4, ['push_front 861', 'push_front -819', 'pop_back',
                        'pop_back'])
    assert res == ['861', '-819']


if __name__ == '__main__':
    main()
