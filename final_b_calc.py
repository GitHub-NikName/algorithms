# обратная польская нотация


class Stack(list):
    def push(self, value):
        self.append(value)


def calc(data: list) -> int:
    stack = Stack()
    for el in data:
        if el.lstrip('+-*/').isdigit():
            stack.push(int(el))
        else:
            if el == '/':
                el += '/'
            x, y = stack.pop(), stack.pop()
            stack.push(eval(f'y {el} x'))
    return stack.pop()


def input_data() -> list:
    return input().split()


def main() -> None:
    data = input_data()
    res = calc(data)
    print(res)


def test():
    res = calc(['2', '1', '+', '3', '*'])
    assert res == 9


if __name__ == '__main__':
    main()
