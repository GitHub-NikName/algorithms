# id: 87182366

from typing import Tuple


class Member:
    def __init__(self, login: str, task: str, fine: str):
        self.login: str = login
        self.task: int = int(task)
        self.fine: int = int(fine)

    def __lt__(self, other):
        self_obj = (- self.task, self.fine, self.login)
        other_obj = (- other.task, other.fine, other.login)
        return self_obj < other_obj

    def __gt__(self, other):
        return other.__lt__(self)

    def __str__(self):
        return self.login


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


if __name__ == '__main__':
    length = int(input())
    array = [Member(*input().split()) for _ in range(length)]
    quicksort(array, 0, length - 1)
    print(*array, sep='\n')
