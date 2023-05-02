# J. Списочная очередь

from typing import Optional


class Node:
    def __init__(self, value: int, next_item=None):
        self.value: int = value
        self.next_item: Node = next_item


class Queue:
    def __init__(self):
        self.__size: int = 0
        self.__head: Optional[Node] = None
        self.__tail: Optional[Node] = None

    def get(self) -> int:
        if self.__size == 0:
            raise IndexError
        x = self.__head.value
        self.__head = self.__head.next_item
        self.__size -= 1
        return x

    def put(self, value: str) -> None:
        value = int(value)
        if self.__size == 0:
            self.__head = Node(value)
            self.__tail = self.__head
        else:
            self.__tail.next_item = Node(value)
            self.__tail = self.__tail.next_item
        self.__size += 1

    def size(self) -> int:
        return self.__size


def input_data() -> list:
    n = int(input())
    return [input() for _ in range(n)]


def que_proc(commands: list) -> list:
    que = Queue()
    result = []
    for el in commands:
        cmd, *val = el.split()
        call = getattr(que, cmd)
        try:
            res = call(*val)
            if res is not None:
                result.append(res)
        except IndexError:
            result.append('error')
    return result


def main() -> None:
    commands = input_data()
    res = que_proc(commands)
    print(*res, sep='\n')


def test():
    res = que_proc(['put -34', 'put -23', 'get', 'size', 'get', 'size', 'get',
                    'get', 'put 80', 'size'])
    assert res == [-34, 1, -23, 0, 'error', 'error', 1]


if __name__ == '__main__':
    main()
