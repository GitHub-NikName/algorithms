# A. Ближайший ноль

from typing import List, Tuple


def input_data() -> Tuple[List[int], int]:
    n = int(input())
    num = list(map(int, input().split()))
    return num, n


def left_distances(num: List[int], n: int) -> List[int]:
    dist = []
    i = 0
    left = float('inf')
    while i < n:
        if not num[i]:
            dist.append(0)
            left = i
        else:
            dist.append(abs(i - left))
        i += 1
    return dist


def algorithm(num: List[int], n: int) -> List[int]:
    result = []
    left = left_distances(num, n)
    right = list(reversed(left_distances(list(reversed(num)), n)))

    i = 0
    while i < n:
        result.append(min(left[i], right[i]))
        i += 1
    return result


def main() -> None:
    num, n = input_data()
    result = algorithm(num, n)
    print(*result)


if __name__ == '__main__':
    main()
