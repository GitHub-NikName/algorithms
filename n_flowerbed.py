from typing import Tuple, List


def input_data() -> Tuple[int, List[List[int]]]:
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    return n, arr


def algorithm(n: int, arr: List[List[int]]) -> List[List[int]]:
    arr = sorted(arr)
    res = []
    start = arr[0][0]
    end = arr[0][1]
    for i in range(1, n):
        if end < arr[i][0]:
            res.append([start, end])
            start = arr[i][0]
            end = arr[i][1]
        elif end < arr[i][1]:
            end = arr[i][1]
    res.append([start, end])
    return res


def test():
    res = algorithm(4, [[7, 8], [7, 8], [2, 3], [6, 10]])
    assert res == [[2, 3], [6, 10]]
    res = algorithm(4, [[2, 3], [5, 6], [3, 4], [3, 4]])
    assert res == [[2, 4], [5, 6]]


def main() -> None:
    n, arr = input_data()
    res = algorithm(n, arr)
    for i in res:
        print(*i)


if __name__ == '__main__':
    main()
