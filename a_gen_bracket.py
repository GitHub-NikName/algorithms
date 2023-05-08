# A. Генератор скобок

class GenBracket:
    def __init__(self, n=None):
        self.__n = n or int(input())
        self.__d = {')': '('}

    def __check(self, seq: str) -> bool:
        if seq[0] == ')':
            return False
        stack = ['']
        for i in seq:
            if stack[-1] == self.__d.get(i):
                stack.pop()
            else:
                stack.append(i)
        return not stack.pop()

    def gen_binary(self, *args) -> None:
        if args:
            n, prefix = args
        else:
            n, prefix = self.__n << 1, ''
        if n == 0:
            if self.__check(prefix):
                print(prefix)
        else:
            self.gen_binary(n - 1, prefix + '(')
            self.gen_binary(n - 1, prefix + ')')


def main():
    a = GenBracket(3)
    a.gen_binary()


if __name__ == '__main__':
    main()
