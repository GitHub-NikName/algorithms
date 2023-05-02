# Очередь на кольцевом буфере.
# I. Ограниченная очередь


from typing import Tuple, Optional, Union


class MyQueueSized:
    def __init__(self, n):
        self.__queue: list = [None] * n
        self.__max_size: int = n
        self.__head: int = 0
        self.__tail: int = 0
        self.__size: int = 0

    def push(self, x: str) -> None:
        if self.__size == self.__max_size:
            raise IndexError('error')
        self.__queue[self.__tail] = int(x)
        self.__tail = self.__get_index(self.__tail)
        self.__size += 1

    def pop(self) -> int:
        if self.__size == 0:
            raise IndexError('None')
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self.__get_index(self.__head)
        self.__size -= 1
        return x

    def peek(self) -> int:
        if self.__size == 0:
            raise IndexError('None')
        return self.__queue[self.__head]

    def size(self) -> int:
        return self.__size

    def __get_index(self, index: int) -> int:
        return (index + 1) % self.__max_size


def input_data() -> Tuple[int, list]:
    n = int(input())
    max_size = int(input())
    data = [input() for _ in range(n)]
    return max_size, data


def make_magik(queue: MyQueueSized, el: str) -> Optional[Union[str, int]]:
    cmd, *val = el.split()
    call = getattr(queue, cmd)
    try:
        return call(*val)
    except IndexError as e:
        return e.args[0]


def algorithm(max_size: int, data: list) -> list:
    queue = MyQueueSized(max_size)
    result = []
    for el in data:
        res = make_magik(queue, el)
        if res is not None:
            result.append(res)
    return result


def main() -> None:
    max_size, data = input_data()
    res = algorithm(max_size, data)
    print(*res, sep='\n')


def test():
    res = algorithm(2, ['peek', 'push 5', 'push 2', 'peek', 'size', 'size',
                        'push 1', 'size'])
    assert res == ['None', 5, 2, 2, 'error', 2]


if __name__ == '__main__':
    main()
