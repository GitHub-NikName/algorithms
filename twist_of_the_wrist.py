# B. Ловкость рук

from collections import Counter
from typing import Tuple


def input_data() -> Tuple[str, int]:
    k = int(input()) * 2
    num = ''.join([input().replace('.', '') for _ in range(4)])
    return num, k


def algorithm(num: str, k: int) -> int:
    num = Counter(map(int, num))
    result = 0
    i = 1
    while i <= 9:
        cnt = num.get(i)
        if cnt and cnt <= k:
            result += 1
        i += 1
    return result


def main() -> None:
    num, k = input_data()
    result = algorithm(num, k)
    print(result)


if __name__ == '__main__':
    main()
