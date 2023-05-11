# id: 87159648

from typing import Tuple, List


class Member:
    def __init__(self, login: str, task: str, fine: str):
        self.login: str = login
        self.task: int = int(task)
        self.fine: int = int(fine)

    def __lt__(self, other):
        obj_1 = (- self.task, self.fine, self.login)
        obj_2 = (- other.task, other.fine, other.login)
        return obj_1 < obj_2

    def __gt__(self, other):
        obj_1 = (- self.task, self.fine, self.login)
        obj_2 = (- other.task, other.fine, other.login)
        return obj_1 > obj_2

    def __str__(self):
        return self.login


def input_data() -> Tuple[int, List[Member]]:
    n = int(input())
    arr = [Member(*input().split()) for _ in range(n)]
    return n, arr


def partition(arr: list, low: int, high: int) -> Tuple[int, int]:
    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    return low, high


def quicksort(arr: list, low: int, high: int) -> None:
    if high <= low:
        return
    else:
        left, right = partition(arr, low, high)
        quicksort(arr, low, right)
        quicksort(arr, left, high)


def main() -> None:
    n, arr = input_data()
    quicksort(arr, 0, n - 1)
    print(*arr, sep='\n')


if __name__ == '__main__':
    main()
