# A. Мониторинг

from typing import Tuple, List


def input_data() -> Tuple[int, List[List[str]]]:
    n = int(input())
    m = int(input())
    matrix = [input().split() for _ in range(n)]
    return m, matrix


def algorithm(m: int, matrix: list) -> List[List[str]]:
    res = []
    for j in range(m):
        row = []
        for i in matrix:
            row.append(i[j])
        res.append(row)
    return res


def main():
    m, matrix = input_data()
    res = algorithm(m, matrix)
    for row in res:
        print(*row)


def test():
    res = algorithm(3, [
        [1, 2, 3],
        [0, 2, 6],
        [7, 4, 1],
        [2, 7, 0]
    ])
    assert res == [[1, 0, 7, 2], [2, 2, 4, 7], [3, 6, 1, 0]]

    res = algorithm(5, [
        [-7, -1, 0, -4, -9],
        [5, -1, 2, 2, 9],
        [3, 1, -8, -1, -7],
        [9, 0, 8, -8, -1],
        [2, 4, 5, 2, 8],
        [-7, 10, 0, -4, -8],
        [-3, 10, -7, 10, 3],
        [1, 6, -7, -5, 9],
        [-1, 9, 9, 1, 9]
    ])
    assert res == [
        [-7, 5, 3, 9, 2, -7, -3, 1, -1],
        [-1, -1, 1, 0, 4, 10, 10, 6, 9],
        [0, 2, -8, 8, 5, 0, -7, -7, 9],
        [-4, 2, -1, -8, 2, -4, 10, -5, 1],
        [-9, 9, -7, -1, 8, -8, 3, 9, 9]
    ]


if __name__ == '__main__':
    main()
