from typing import Tuple, List


def input_data() -> Tuple[int, List[str]]:
    return int(input()), input().split()


def less(obj_1: str, obj_2: str) -> bool:
    if len(obj_1) == len(obj_2):
        return obj_1 > obj_2
    return obj_1 + obj_2 > obj_2 + obj_1


def algorithm(n: int, arr: List[str]) -> str:
    for i in range(1, n):
        item_to_insert = arr[i]
        j = i
        while j > 0 and less(item_to_insert, arr[j - 1]):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item_to_insert
    return ''.join(arr)


def main() -> None:
    n, arr = input_data()
    res = algorithm(n, arr)
    print(''.join(res))


def test():
    assert algorithm(3, ['15', '56', '2']) == '56215'
    assert algorithm(3, ['1', '783', '2']) == '78321'
    assert algorithm(5, ['2', '4', '5', '2', '10']) == '542210'
    assert algorithm(6, ['9', '10', '1', '1', '1', '6']) == '9611110'


if __name__ == '__main__':
    # main()
    test()
