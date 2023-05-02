# Число фибоначчи по модулю.
# Матрица и быстрый алгоритм.


class FiboMatrix:
    def __init__(self, m, k):
        self.data = m
        self.k = k
        self.mod = 10 ** k

    def __matmul__(self, y):
        ans = self.copy()
        ans @= y
        return ans

    def __imatmul__(self, y):
        self.data = [[sum((a * b) % self.mod for a, b in zip(row_a, col_b))
                      for col_b in zip(*y.data)] for row_a in self.data]
        return self

    def __pow__(self, exp):
        cur = FiboMatrix([[1, 0],[ 0, 1]], self.k)
        base = self.copy()
        while exp:
            if exp & 1:
                exp -= 1
                cur @= base
            else:
                exp >>= 1
                base @= base
        return cur

    def copy(self):
        return FiboMatrix(self.data, self.k)


def fib_mod(n, k):
    fib_mat = FiboMatrix([[0, 1], [1, 1]], k)
    fib_pow = fib_mat ** n
    return fib_pow.data[1][1] % 10 ** k


def input_data() -> list:
    return list(map(int, input().split()))


def main() -> None:
    n, k = input_data()
    res = fib_mod(n, k)
    print(res)


def test():
    assert fib_mod(3, 1) == 3
    assert fib_mod(10, 1) == 9
    assert fib_mod(70, 6) == 170129
    assert fib_mod(237, 7) == 471519


if __name__ == '__main__':
    main()


# fast algorithm

def fib_mod(n, mod):
    if n == 0:
        return 0, 1
    else:
        a, b = fib_mod(n // 2, mod)
        c = a * (b * 2 - a)
        d = a * a + b * b
    if n & 1:
        return d % mod, (c + d) % mod
    return c % mod, d % mod


def input_data() -> list:
    return list(map(int, input().split()))


def main() -> None:
    n, k = input_data()
    mod = 10 ** k
    res = fib_mod(n, mod)[1]
    print(res)


def test():
    # mod = 10 ** k
    assert fib_mod(3, 10)[1] == 3
    assert fib_mod(10, 10)[1] == 9
    assert fib_mod(70, 1000000)[1] == 170129
    assert fib_mod(237, 10000000)[1] == 471519


if __name__ == '__main__':
    main()
