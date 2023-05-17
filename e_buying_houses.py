def count_house(arr: list, n: int, k: int) -> int:
    cnt = 0
    arr.sort()
    while cnt < n and k >= arr[cnt]:
        k -= arr[cnt]
        cnt += 1
    return cnt


def test():
    assert count_house([999, 999, 999], 3, 300) == 0
    assert count_house([350, 999, 200], 3, 1000) == 2
    assert count_house([3], 1, 4)


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(count_house(arr, n, k))
