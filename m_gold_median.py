def main(n, m, north, south):
    lf = 0
    rh = 0
    length = n + m
    mid = length // 2 + 1

    def median():
        nonlocal lf, rh, mid
        for i in range(2, mid + 2):
            if lf < n and rh < m:
                if north[lf] < south[rh]:
                    if i >= mid:
                        yield north[lf]
                    lf += 1

                else:
                    if i >= mid:
                        yield south[rh]
                    rh += 1

            elif lf < n:
                if i >= mid:
                    yield north[lf]
                lf += 1

            else:
                if i >= mid:
                    yield south[rh]
                rh += 1

    arr = list(median())
    return arr[-1] if length & 1 else (sum(arr)) / 2


if __name__ == '__main__':
    n, m = [int(input()) for _ in range(2)]
    north, south = [list(map(int, input().split())) for _ in range(2)]
    print(main(n, m, north, south))
