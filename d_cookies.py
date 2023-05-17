
def happy_children(n: int, greed: list, m: int, cookies: list) -> int:
    cnt = 0
    ch_index = 0
    cookies_index = 0
    greed.sort()
    cookies.sort()
    while cookies_index < m and ch_index < n:
        if cookies[cookies_index] >= greed[ch_index]:
            cnt += 1
            ch_index += 1
        cookies_index += 1
    return cnt


def test():
    assert happy_children(2, [1, 2], 3, [2, 1, 3]) == 2
    assert happy_children(3, [2, 1, 3], 2, [1, 1]) == 1


if __name__ == '__main__':
    n = int(input())
    greed_factor = list(map(int, input().split()))
    m = int(input())
    size_cookies = list(map(int, input().split()))
    res = happy_children(n, greed_factor, m, size_cookies)
    print(res)
